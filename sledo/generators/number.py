import click
from random import randrange
from sledo.generators.base import FieldGenerator


class NumberGenerator(FieldGenerator):
    def generate(self, field: dict, schema_name:str, field_name:str) -> int | float:
        min = field.get("min", 0)
        
        max = field.get("max")
        
        if(max == None):
            click.UsageError(f"Attribute 'max' value required at {schema_name}.{field_name}").show()
            exit(1)    
        
        random_value = randrange(min,max)
        

        return random_value
