from typing import Dict


from .schema import SchemaFieldGenerator
from .base import FieldGenerator
from .number import NumberFieldGenerator
from .date import DateFieldGenerator
from .country import CountryFieldGenerator
from .reference import to_ref

generators: Dict[str, FieldGenerator] = {
    "number": NumberFieldGenerator,
    "date": DateFieldGenerator,
    "country": CountryFieldGenerator
}


def getGeneratorFromFieldType(field_type: str, field_options: Dict[str, str]) -> FieldGenerator:
    Generator = generators.get(field_type, SchemaFieldGenerator)

    return Generator(field_options, field_type)


def get_value_by_attr_name(attr_name: str, schema_name: str, res: Dict = {}, iter_res={}):
    schema = iter_res.get(schema_name, res.get(schema_name))
    if schema is None:
        raise Exception(
            f"Cannot find schema: '{schema_name}' in current result")

    entries = list(filter(
        lambda header: header[1][0] == attr_name, enumerate(schema[0])))

    if len(entries) == 0:
        raise Exception(f"Cannot find attribute: '{attr_name}'")

    entry = entries[0]

    # check if the entry is a schema field generator
    generator = getattr(entry[1][1], "__self__", None)
    if generator is not None and isinstance(generator, SchemaFieldGenerator):
        # find the referenced schema
        return generator.schema

    return schema[1][-1][entry[0]]
