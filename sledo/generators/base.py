from abc import ABC, abstractmethod


class FieldGenerator(ABC):
    @abstractmethod
    def id(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def generate(self, field: dict):
        raise NotImplementedError()
