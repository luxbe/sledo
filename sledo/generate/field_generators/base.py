from abc import ABCMeta, abstractmethod
from typing import Any, Dict, Tuple


class FieldGenerator(object, metaclass=ABCMeta):
    def __init__(self, options: Dict[str, str] = None, type: str = None):
        super(FieldGenerator, self).__init__()
        self.options = options
        self.type = type
        self.validate()

    @abstractmethod
    def validate(self):
        raise NotImplementedError()

    @abstractmethod
    def generate(self):
        raise NotImplementedError()

    def generate_str(self, *args) -> str:
        return str(self.generate(*args))
