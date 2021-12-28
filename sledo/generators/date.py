from datetime import timedelta
from random import randrange
from sledo.exceptions import MissingAttributeError, AttributeError
from sledo.generators.base import FieldGenerator


class DateGenerator(FieldGenerator):
    def generate(self, field: dict, schema_name: str, field_name: str) -> int | float:
        min = field.get("min")
        max = field.get("max")

        if(min == None):
            raise MissingAttributeError('min', schema_name, field_name)

        if(max == None):
            raise MissingAttributeError('max', schema_name, field_name)

        if(max < min):
            raise AttributeError(
                'max', "must be greater than attribute 'min'", schema_name, field_name)

        day_difference = (max - min).days

        random_date = min+timedelta(days=randrange(day_difference+1))

        return random_date
