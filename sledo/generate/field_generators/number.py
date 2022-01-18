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

    def generate(self, **kwargs):
        self.prepare_options(**kwargs)
        min: float = self.options["min"]
        max: float = self.options["max"]

        if max < min:
            raise Exception(
                f"'max' ({self.options['max']}) must be equal or larger than 'min' ({self.options['min']})")

        digits: int = self.options["digits"]

        return float(f"{((random() * (max - min)) + min):.{digits}f}")

    def val_to_str(self, value: Any) -> str:
        digits: int = self.options["digits"]

        return f"{value:.{digits}f}"
