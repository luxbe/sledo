from schema import Schema

from .base import FieldGenerator


class SchemaFieldGenerator(FieldGenerator):
    option_schema = Schema({})

    def validate(self):
        self.option_schema.validate(self.options)

    def generate(self, res):
        schema = res.get(self.type)

        if schema is None:
            raise Exception(f"Schema '{self.type}' is not generated yet")

        # return id of latest schema
        return schema[1][-1][0][0]
