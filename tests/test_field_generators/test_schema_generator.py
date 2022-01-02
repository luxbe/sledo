from datetime import date
import unittest
from schema import SchemaError
from sledo.generate.field_generators.schema import SchemaFieldGenerator


class TestSchemaFieldGenerator(unittest.TestCase):
    def test_validation_no_keys(self):
        SchemaFieldGenerator()

    def test_validation_unknown_keys(self):
        with self.assertRaises(SchemaError) as ctx:
            SchemaFieldGenerator({"invalid": "invalid"})
        self.assertTrue("None does not match" in ctx.exception.code,
                        "No options should be passed")

    def test_generation(self):
        step_res = {
            "Test1": (("id", "amount", "date"), [
                [2, 6, date(2020, 1, 20)],
            ]),
            "Test2": (("id", "amount", "date"), [
                [4, 3, date(2020, 2, 18)],
            ]),
        }

        with self.assertRaises(Exception) as ctx:
            SchemaFieldGenerator(type="Test").generate(step_res)
        self.assertTrue(
            "Schema 'Test' is not generated yet" in str(ctx.exception))

        generator = SchemaFieldGenerator(type="Test1")
        self.assertEqual(generator.generate(step_res), 2)

        generator = SchemaFieldGenerator(type="Test2")
        self.assertEqual(generator.generate(step_res), 4)
