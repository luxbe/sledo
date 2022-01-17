from typing import Any
from schema import Or, Schema, Use, Optional
import random

from .reference import to_ref
from .base import FieldGenerator


class StringFieldGenerator(FieldGenerator):
    option_schema = Schema({
        "source": Or(Use(to_ref), Use(str))
        # Optional("source", default=None): Use(str)
    })

    def validate(self):
        self.options = self.option_schema.validate(self.options)

    def generate(self, res={}):
        options = self.prepare_options(res)

        source: str = options["source"]

        lines=open(source).read().splitlines()
        return random.choice(lines)
            
