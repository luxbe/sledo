import click
from datetime import date, datetime, timedelta
from random import randrange
from sledo.generators.base import FieldGenerator


class DateGenerator(FieldGenerator):
    def generate(self, field: dict, schema_name:str, field_name:str) -> int | float:
        min = field.get("min")
        max = field.get("max")

        if(max == None):
            click.UsageError(f"Attribute 'max' required at {schema_name}.{field_name}").show()
            exit(1) 
        if(min == None):
            click.UsageError(f"Attribute 'min' required at {schema_name}.{field_name}").show()
            exit(1) 
        
        if(max<min):
            click.UsageError(f"Attribute 'max' must be greater than attribute 'min' at {schema_name}.{field_name}").show()
            exit(1) 
        day_difference = (max - min).days

        random_date = min+timedelta(days=randrange(day_difference+1))
        
        return random_date
