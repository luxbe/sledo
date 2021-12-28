
from typing import Dict

from sledo.generators.base import FieldGenerator
from sledo.generators.date import DateGenerator

from sledo.generators.number import NumberGenerator

generator_dict: Dict[str, FieldGenerator] = {
    "number": NumberGenerator(),
    "date": DateGenerator(),
}


def generate(field: str | dict, schema_name: str, field_name: str):
    field_type = field if type(field) is str else field.get("type")
    field_conf = {} if type(field) is str else field

    generator = generator_dict.get(field_type)

    if generator is None:
        return None

    return generator.generate(field_conf, schema_name, field_name)
