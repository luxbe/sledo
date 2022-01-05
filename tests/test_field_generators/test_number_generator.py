import pytest
from schema import SchemaError
from sledo.generate.field_generators.number import NumberFieldGenerator


# class TestNumberFieldGenerator(unittest.TestCase):
def test_validation_no_keys():
    with pytest.raises(SchemaError) as ctx:
        NumberFieldGenerator({})
    assert "Missing keys: 'max', 'min'" in str(
        ctx.value), "Expected the keys 'max' and 'min' to be required"


def test_validation_optional_keys():
    generator = NumberFieldGenerator({"min": 0, "max": 1})
    assert generator.options["digits"] == 0
    assert ["min", "max", "digits"] == [
        *generator.options], "Expected the keys 'max', 'min', and 'digits' to be defined"

    generator = NumberFieldGenerator({"min": 0, "max": 1, "digits": 2})
    assert generator.options["digits"] == 2


def test_validation_key_parsing():
    generator = NumberFieldGenerator({"min": 0, "max": 0.5})
    assert generator.options["min"] == 0
    assert generator.options["max"] == 0.5

    generator = NumberFieldGenerator({"min": "1", "max": "2.7"})
    assert generator.options["min"] == 1
    assert generator.options["max"] == 2.7

    with pytest.raises(SchemaError):
        NumberFieldGenerator({"min": 0, "max": {}})

    with pytest.raises(SchemaError):
        NumberFieldGenerator({"min": "a", "max": 0})

    with pytest.raises(SchemaError):
        NumberFieldGenerator({"min": 0, "max": []})


# def test_validation_key_relation():
#     NumberFieldGenerator({"min": 0, "max": 2})
#     NumberFieldGenerator({"min": 0, "max": 0})

#     with pytest.raises(SchemaError):
#         NumberFieldGenerator({"min": 1, "max": 0})


def test_generation():
    generator = NumberFieldGenerator({
        "min": 4,
        "max": 6
    })

    res = generator.generate()
    assert type(res) is float
    assert 4 <= res <= 6

    generator = NumberFieldGenerator({
        "min": 4,
        "max": 6,
        "digits": 2
    })

    res = generator.val_to_str(generator.generate())
    assert len(res) == 4


def test_generation_stress_test():
    generator = NumberFieldGenerator({
        "min": 4,
        "max": 6,
        "digits": 2
    })

    res = []
    for _ in range(100_000):
        res.append(generator.generate())

    assert min(res) >= 4
    assert max(res) <= 6
