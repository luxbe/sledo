from datetime import date
import pytest
from schema import SchemaError
from sledo.generate.field_generators.date import DateFieldGenerator


def test_validation_no_keys():
    with pytest.raises(SchemaError) as ctx:
        DateFieldGenerator({})
    assert "Missing keys: 'max', 'min'" in str(
        ctx.value), "Expected the keys 'max' and 'min' to be required"


def test_validation_key_parsing():
    generator = DateFieldGenerator(
        {"min": "2020-01-01", "max": "2020-01-10"})
    assert generator.options["min"] == date(2020, 1, 1)
    assert generator.options["max"] == date(2020, 1, 10)

    with pytest.raises(SchemaError):
        DateFieldGenerator({"min": 0, "max": {}})

    with pytest.raises(SchemaError):
        DateFieldGenerator({"min": "a", "max": 0})

    with pytest.raises(SchemaError):
        DateFieldGenerator({"min": "2020/29/29", "max": []})

# def test_validation_key_relation():
#     DateFieldGenerator({"min": "2020-01-01", "max": "2020-01-10"})
#     DateFieldGenerator({"min": "2020-01-01", "max": "2020-01-01"})

#     with pytest.raises(SchemaError) as ctx:
#         DateFieldGenerator({"min": "2020-01-10", "max": "2020-01-01"})


def test_generation():
    generator = DateFieldGenerator(
        {"min": "2020-01-01", "max": "2020-01-10"})

    res = generator.generate()
    assert type(res) is date


def test_generation_stress_test():
    generator = DateFieldGenerator(
        {"min": "2020-01-01", "max": "2020-01-10"})

    res = []
    for _ in range(100_000):
        res.append(generator.generate())

    assert min(res) >= date(2020, 1, 1)
    assert max(res) <= date(2020, 1, 10)
