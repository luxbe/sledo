from datetime import date, timedelta
from schema import Schema, SchemaError, Use
from random import randint

from .base import FieldGenerator


class DateFieldGenerator(FieldGenerator):
    option_schema = Schema({
        "min": Use(date.fromisoformat),
        "max": Use(date.fromisoformat)
    })

    def validate(self):
        self.options = self.option_schema.validate(self.options)

        if self.options["max"] < self.options["min"]:
            raise SchemaError(
                f"'max' ({self.options['max']}) must be equal or larger than 'min' ({self.options['min']})")

    def generate(self):
        min = self.options["min"]
        max = self.options["max"]

        day_difference = (max - min).days

        random_date = min + timedelta(days=randint(0, day_difference))

        return random_date
