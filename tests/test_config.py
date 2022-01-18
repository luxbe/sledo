
from typing import Dict
import pytest
from schema import SchemaError
import yaml

from sledo.generate.config import validateConfig

base_config: Dict = {}

with open("tests/resources/config.yaml") as f:
    base_config = yaml.load(f, Loader=yaml.BaseLoader)


def test_validation_no_keys():
    with pytest.raises(SchemaError) as ctx:
        validateConfig({})
    assert "Missing key: 'schemas'" in str(
        ctx.value), "Expected the key 'schemas' to be required"


def test_validation_initial():
    config = dict(base_config)
    config["initial"] = "invalid"
    with pytest.raises(SchemaError) as ctx:
        validateConfig(config)
    assert "Missing step: 'invalid'" in str(ctx.value)


def test_validation_steps_generate():
    config = dict(base_config)
    config["steps"]["create_order"]["generate"] = "invalid"
    with pytest.raises(SchemaError) as ctx:
        validateConfig(config)
    assert "Missing schema: 'invalid'" in str(ctx.value)


def test_validation_steps_generate_probability():
    config = dict(base_config)
    config["steps"]["create_order"]["generate"] = {
        "Invoice": 0.7,
        "Order": 0.6
    }
    with pytest.raises(SchemaError) as ctx:
        validateConfig(config)
    assert "The total probability must not be more than 1 at step: 'create_order'" in str(
        ctx.value)
