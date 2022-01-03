from datetime import date
import unittest
from schema import SchemaError
from sledo.generate.field_generators.date import DateFieldGenerator


class TestDateFieldGenerator(unittest.TestCase):
    def test_validation_no_keys(self):
        with self.assertRaises(SchemaError) as ctx:
            DateFieldGenerator({})
        self.assertTrue("Missing keys: 'max', 'min'" in ctx.exception.code,
                        "The keys 'max' and 'min' should be required")

    def test_validation_key_parsing(self):
        generator = DateFieldGenerator(
            {"min": "2020-01-01", "max": "2020-01-10"})
        self.assertEqual(generator.options["min"], date(2020, 1, 1))
        self.assertEqual(generator.options["max"], date(2020, 1, 10))

        with self.assertRaises(SchemaError) as ctx:
            DateFieldGenerator({"min": 0, "max": {}})
            DateFieldGenerator({"min": "a", "max": 0})
            DateFieldGenerator({"min": "2020/29/29", "max": []})

    # def test_validation_key_relation(self):
    #     DateFieldGenerator({"min": "2020-01-01", "max": "2020-01-10"})
    #     DateFieldGenerator({"min": "2020-01-01", "max": "2020-01-01"})

    #     with self.assertRaises(SchemaError) as ctx:
    #         DateFieldGenerator({"min": "2020-01-10", "max": "2020-01-01"})

    def test_generation(self):
        generator = DateFieldGenerator(
            {"min": "2020-01-01", "max": "2020-01-10"})

        res = generator.generate()
        self.assertTrue(type(res) is date,
                        "The generated date should be of type 'date'")

    def test_generation_stress_test(self):
        generator = DateFieldGenerator(
            {"min": "2020-01-01", "max": "2020-01-10"})

        res = []
        for _ in range(100_000):
            res.append(generator.generate())

        self.assertTrue(min(res) >= date(2020, 1, 1))
        self.assertTrue(max(res) <= date(2020, 1, 10))
