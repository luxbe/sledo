from datetime import date
import pytest
from schema import SchemaError
from sledo.generate.field_generators.schema import SchemaFieldGenerator


def test_validation_no_keys():
    SchemaFieldGenerator()


def test_validation_unknown_keys():
    with pytest.raises(SchemaError) as ctx:
        SchemaFieldGenerator({"invalid": "invalid"})
    assert "Wrong key" in str(ctx.value), "Expected no options to be passable"


def test_generation():
    step_res = {
        "Test1": (("id", "amount", "date"), [
            [(2, str), (6, str), (date(2020, 1, 20), str)],
        ]),
        "Test2": (("id", "amount", "date"), [
            [(4, str), (3, str), (date(2020, 2, 18), str)],
        ]),
    }

    with pytest.raises(Exception) as ctx:
        SchemaFieldGenerator(type="Test").generate(step_res)
    assert "Schema 'Test' is not generated yet" in str(ctx.value)

    generator = SchemaFieldGenerator(type="Test1")
    assert generator.generate(step_res) == 2

    generator = SchemaFieldGenerator(type="Test2")
    assert generator.generate(step_res) == 4
