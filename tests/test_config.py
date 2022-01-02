
import unittest
from schema import SchemaError

from sledo.generate.config import validateConfig


class TestConfigFieldGenerator(unittest.TestCase):
    def test_validation_no_keys(self):
        with self.assertRaises(SchemaError) as ctx:
            validateConfig({})
        self.assertTrue("Missing keys: 'amount', 'initial', 'schemas', 'steps'" in ctx.exception.code,
                        "The keys 'amount', 'initial', 'schemas', 'steps' should be required")
