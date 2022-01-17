from abc import ABCMeta, abstractmethod
from typing import Any, Dict, List, Tuple

from .reference import ReferenceFieldGenerator


class FieldGenerator(object, metaclass=ABCMeta):
    def __init__(self, options: Dict[str, str] = {}, type: str = None):
        super(FieldGenerator, self).__init__()
        self.options = options
        self.type = type
        self.validate()

    @abstractmethod
    def validate(self):
        raise NotImplementedError()

    @abstractmethod
    def generate(self, res: Dict[str, Tuple[Tuple, List[List]]] = {}):
        raise NotImplementedError()

    def val_to_str(self, value: Any) -> str:
        return str(value)

    def prepare_options(self, res: Dict[str, Tuple[Tuple, List[List]]]):
        options = self.options.copy()
        for (key, value) in self.options.items():
            if not isinstance(value, ReferenceFieldGenerator):
                continue

            schema = res[value.type]
            index = schema[0].index(value.options["field_attr"])

            options[key] = schema[1][-1][index][0]

        return options
