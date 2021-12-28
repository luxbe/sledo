
from typing import Dict

import click
from sledo.generators.base import FieldGenerator
from sledo.generators.date import DateGenerator

from sledo.generators.number import NumberGenerator

generator_dict: Dict[str, FieldGenerator] = {
    "number": NumberGenerator(),
    "date": DateGenerator(),
}


def generate(field: dict):
    type = field.get("type")
    generator = generator_dict.get(type)

    if generator is None:
        click.UsageError(f"Can't find generator '{type}'").show()
        exit(1)

    return generator.generate(field)
