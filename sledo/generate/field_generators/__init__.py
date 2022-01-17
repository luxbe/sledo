from typing import Dict

from .schema import SchemaFieldGenerator
from .base import FieldGenerator
from .number import NumberFieldGenerator
from .date import DateFieldGenerator
from .stringFromFile import StringFieldGenerator


generators: Dict[str, FieldGenerator] = {
    "number": NumberFieldGenerator,
    "date": DateFieldGenerator,
    "string_from_file": StringFieldGenerator
}


def getGeneratorFromFieldType(field_type: str, field_options: Dict[str, str]) -> FieldGenerator:
    Generator = generators.get(field_type, SchemaFieldGenerator)

    return Generator(field_options, field_type)
