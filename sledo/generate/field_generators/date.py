from datetime import date, timedelta
from schema import Or, Schema, Use
from random import randint

from .reference import to_ref
from .base import FieldGenerator


class DateFieldGenerator(FieldGenerator):
    option_schema = Schema({
        "min": Or(Use(to_ref), Use(date.fromisoformat)),
        "max": Or(Use(to_ref), Use(date.fromisoformat))
    })

    def validate(self):
        self.options = self.option_schema.validate(self.options)

        # if self.options["max"] < self.options["min"]:
        #     raise SchemaError(
        #         f"'max' ({self.options['max']}) must be equal or larger than 'min' ({self.options['min']})")

    def generate(self, res={}):
        options = self.prepare_options(res)
        min = options["min"]
        max = options["max"]

        day_difference = (max - min).days

        return min + timedelta(days=randint(0, day_difference))
