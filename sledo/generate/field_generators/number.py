from typing import Any
from schema import Or, Schema, Use, Optional
from random import random

from .reference import to_ref
from .base import FieldGenerator


class NumberFieldGenerator(FieldGenerator):
    option_schema = Schema({
        "min": Or(Use(to_ref), Use(float)),
        "max": Or(Use(to_ref), Use(float)),
        Optional("digits", default=0): Use(int)
    })

    def validate(self):
        self.options = self.option_schema.validate(self.options)

        # if self.options["max"] < self.options["min"]:
        #     raise SchemaError(
        #         f"'max' ({self.options['max']}) must be equal or larger than 'min' ({self.options['min']})")

    def generate(self, res={}):
        options = self.prepare_options(res)

        min: float = options["min"]
        max: float = options["max"]

        return (random() * (max - min)) + min

    def val_to_str(self, value: Any) -> str:
        digits: int = self.options["digits"]

        return f"{value:.{digits}f}"
