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
    iter_res = {
        "Test1": ((("id", str), ("amount", str), ("date", str)), [
            [2, 6, date(2020, 1, 20)],
        ]),
        "Test2": ((("id", str), ("amount", str), ("date", str)), [
            [4, 3, date(2020, 2, 18)],
        ]),
    }

    with pytest.raises(Exception) as ctx:
        SchemaFieldGenerator(type="Test").generate(iter_res=iter_res)
    assert "Schema 'Test' is not generated yet" in str(ctx.value)

    generator = SchemaFieldGenerator(type="Test1")
    assert generator.generate(iter_res=iter_res) == 2

    generator = SchemaFieldGenerator(type="Test2")
    assert generator.generate(iter_res=iter_res) == 4
