
from typing import Dict
import unittest
from schema import SchemaError
import yaml

from sledo.generate.config import validateConfig


class TestConfigFieldGenerator(unittest.TestCase):
    config: Dict

    def setUp(self) -> Dict:
        super().setUp()
        with open("tests/resources/config.yaml") as f:
            self.config = yaml.load(f, Loader=yaml.BaseLoader)

    def test_validation_no_keys(self):
        with self.assertRaises(SchemaError) as ctx:
            validateConfig({})
        self.assertTrue("Missing keys: 'amount', 'initial', 'schemas', 'steps'" in ctx.exception.code,
                        "The keys 'amount', 'initial', 'schemas', 'steps' should be required")

    def test_validation_initial(self):
        config = dict(self.config)
        config["initial"] = "invalid"
        with self.assertRaises(SchemaError) as ctx:
            validateConfig(config)
        self.assertTrue("Missing step: 'invalid'" in ctx.exception.code)

    def test_validation_steps_generate(self):
        config = dict(self.config)
        config["steps"]["create_order"]["generate"] = "invalid"
        with self.assertRaises(SchemaError) as ctx:
            validateConfig(config)
        self.assertTrue("Missing schema: 'invalid'" in ctx.exception.code)

    def test_validation_steps_generate_probability(self):
        config = dict(self.config)
        config["steps"]["create_order"]["generate"] = {
            "Invoice": 0.7,
            "Order": 0.6
        }
        with self.assertRaises(SchemaError) as ctx:
            validateConfig(config)
        self.assertTrue(
            "The total probability must not be more than 1 at step: 'create_order'" in ctx.exception.code)
