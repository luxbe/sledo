from schema import Schema, SchemaError, Use, Optional
from random import random

from .base import FieldGenerator


class NumberFieldGenerator(FieldGenerator):
    option_schema = Schema({
        "min": Use(float),
        "max": Use(float),
        Optional("digits", default=0): Use(int)
    })

    def validate(self):
        self.options = self.option_schema.validate(self.options)

        if self.options["max"] < self.options["min"]:
            raise SchemaError(
                f"'max' ({self.options['max']}) must be equal or larger than 'min' ({self.options['min']})")

    def generate(self):
        min: float = self.options["min"]
        max: float = self.options["max"]
        digits: int = self.options["digits"]

        random_value = (random() * (max - min)) + min

        return f"{random_value:.{digits}f}"
