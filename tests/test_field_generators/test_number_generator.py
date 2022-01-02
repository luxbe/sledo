import unittest
from schema import SchemaError
from sledo.generate.field_generators.number import NumberFieldGenerator


class TestNumberFieldGenerator(unittest.TestCase):
    def test_validation_no_keys(self):
        with self.assertRaises(SchemaError) as ctx:
            NumberFieldGenerator({})
        self.assertTrue("Missing keys: 'max', 'min'" in ctx.exception.code,
                        "The keys 'max' and 'min' should be required")

    def test_validation_optional_keys(self):
        generator = NumberFieldGenerator({"min": 0, "max": 1})
        self.assertEqual(
            generator.options["digits"], 0, "The key 'digits' should default to 0")
        self.assertEqual(["min", "max", "digits"], [*
                         generator.options], "All keys should be included")

        generator = NumberFieldGenerator({"min": 0, "max": 1, "digits": 2})
        self.assertEqual(generator.options["digits"], 2)

    def test_validation_key_parsing(self):
        generator = NumberFieldGenerator({"min": 0, "max": 0.5})
        self.assertEqual(generator.options["min"], 0)
        self.assertEqual(generator.options["max"], 0.5)

        generator = NumberFieldGenerator({"min": "1", "max": "2.7"})
        self.assertEqual(generator.options["min"], 1)
        self.assertEqual(generator.options["max"], 2.7)

        with self.assertRaises(SchemaError) as ctx:
            NumberFieldGenerator({"min": 0, "max": {}})
            NumberFieldGenerator({"min": "a", "max": 0})
            NumberFieldGenerator({"min": 0, "max": []})

    def test_validation_key_relation(self):
        NumberFieldGenerator({"min": 0, "max": 2})
        NumberFieldGenerator({"min": 0, "max": 0})

        with self.assertRaises(SchemaError) as ctx:
            NumberFieldGenerator({"min": 1, "max": 0})

    def test_generation(self):
        generator = NumberFieldGenerator({
            "min": 4,
            "max": 6
        })

        res = generator.generate()
        self.assertTrue(type(res) is float,
                        "The generated number should be of type 'float'")
        self.assertTrue(4 <= res <= 6)

        generator = NumberFieldGenerator({
            "min": 4,
            "max": 6,
            "digits": 2
        })

        res = generator.generate_str()
        self.assertEqual(
            len(res), 4, "The generated number should be 4 chararcters long")

    def test_generation_stress_test(self):
        generator = NumberFieldGenerator({
            "min": 4,
            "max": 6,
            "digits": 2
        })

        res = []
        for _ in range(100_000):
            res.append(generator.generate())

        self.assertTrue(min(res) >= 4)
        self.assertTrue(max(res) <= 6)
