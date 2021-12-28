
from sledo.generators.base import FieldGenerator


class NumberGenerator(FieldGenerator):
    def id(self) -> str:
        return "number"

    def generate(self, field: dict) -> int | float:
        return 1
