"""
This is the "load_config" module.

The load config helps to load and validate the sledo configuration files.
"""

from schema import And, Or, Schema, Optional, SchemaError, Use
from typing import Dict
import yaml

from sledo.generate.field_generators.base import FieldGenerator
from sledo.generate.field_generators.reference import ReferenceFieldGenerator
from sledo.generate.field_generators.schema import SchemaFieldGenerator
from .field_generators import getGeneratorFromFieldType


class ConfigurationSchema(Schema):
    def validate(self, data, _is_config_schema=True):
        data = super(ConfigurationSchema, self).validate(
            data, _is_config_schema=False)

        if not _is_config_schema:
            return data

        steps: Dict[str, Dict[str, str]] = data["steps"]
        schemas: Dict[str, Dict[str, FieldGenerator]] = data["schemas"]

        # validate initial step
        if steps.get(data["initial"]) is None:
            raise SchemaError(f"Missing step: '{data['initial']}'")

        # validate next steps
        for (key, step) in steps.items():
            next = step.get("next")
            if next is not None and steps.get(next) is None:
                raise SchemaError(f"Missing step: '{next}'")

            generate: str | Dict = step.get("generate")

            if type(generate) is str:
                if schemas.get(generate) is None:
                    raise SchemaError(f"Missing schema: '{schema}'")
            else:
                total_prob = 0
                for (schema, prob) in generate.items():
                    if schemas.get(schema) is None:
                        raise SchemaError(f"Missing schema: '{schema}'")

                    total_prob += prob

                if total_prob > 1:
                    raise SchemaError(
                        f"The total probability must not be more than 1 at step: '{key}'")

        # validate properties
        for schema in schemas.values():
            for value in schema.values():
                if isinstance(value, SchemaFieldGenerator):
                    # check if Schema exists
                    ref = schemas.get(value.type)
                    if ref is None:
                        raise SchemaError(f"Missing schema: '{value.type}'")
                elif isinstance(value, FieldGenerator):
                    for value in value.options.values():
                        if isinstance(value, ReferenceFieldGenerator):
                            ref_field = schema.get(value.options["field"])
                            if ref_field is None:
                                raise SchemaError(
                                    f"Missing attribute: '{value.options['field']}'")

                            if not isinstance(ref_field, SchemaFieldGenerator):
                                raise SchemaError(
                                    f"Attribute '{value.options['field']}' must be a schema reference!")

                            value.type = ref_field.type
                            ref_schema = schemas.get(ref_field.type)
                            ref_schema_field = ref_schema.get(
                                value.options["field_attr"])

                            if ref_schema_field is None:
                                raise SchemaError(
                                    f"Attribute '{value.options['field_attr']}' does not exist in schema {ref_field.type}")
        return data


def to_generator(raw: str | dict):
    is_str = type(raw) is str
    field_type = raw if is_str else raw["type"]
    field_options = {} if is_str else {
        k: raw[k] for k in raw if k != "type"
    }

    generator = getGeneratorFromFieldType(field_type, field_options)

    return generator


# The schema of a valid configuration file
schema = ConfigurationSchema({
    'initial': str,
    'amount': Use(int),
    'steps': {
        str: {
            "generate": Or(str, {
                str: And(Use(float), lambda x: 0 <= x <= 1)
            }),
            Optional("next"): str
        }
    },
    'schemas': {
        str: {
            str: And(Or(str, {
                "type": str,
                str: str
            }), Use(to_generator))
        }
    }
})


def validateConfig(config: Dict):
    return schema.validate(config)


def loadConfig(file: str) -> Dict:
    """
    Loads the configuration file and validates its contents

        Params:
            file (str): the file path of the configuration file

        Returns:
            config (Dict): the loaded configuration file
    """

    # load and parse the configuration file
    with open(file) as f:
        config: Dict = yaml.load(f, Loader=yaml.BaseLoader)

        # validate and transform the loaded configuration file
        return validateConfig(config)
