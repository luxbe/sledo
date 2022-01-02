from typing import Dict, List, Tuple
from schema import Forbidden, Schema

from .base import FieldGenerator


class SchemaFieldGenerator(FieldGenerator):
    option_schema = Schema(None)

    def validate(self):
        self.option_schema.validate(self.options)

    def generate(self, res: Dict[str, Tuple[Tuple, List[List]]]):
        schema = res.get(self.type)

        if schema is None:
            raise Exception(f"Schema '{self.type}' is not generated yet")

        return schema[1][-1][0]
