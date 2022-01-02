from abc import ABCMeta, abstractmethod
from typing import Dict


class FieldGenerator(object, metaclass=ABCMeta):
    # @abstractmethod
    def __init__(self, options: Dict[str, str], type: str):
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
