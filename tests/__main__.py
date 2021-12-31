import unittest

from schema import SchemaError

from sledo.load_config import loadConfig, validateConfig


class TestLoadConfig(unittest.TestCase):
    def test_load_config(self):
        config = loadConfig('./tests/resources/config.yaml')
        self.assertIsNotNone(config, "Config should not be None")

    def test_validate_config(self):
        config = {

        }

        with self.assertRaises(SchemaError) as ctx:
            validateConfig(config)

        self.assertTrue(
            "Missing keys: 'amount', 'initial', 'schemas', 'steps'")


if __name__ == '__main__':
    unittest.main()
