from abc import ABC, abstractmethod


class FieldGenerator(ABC):
    @abstractmethod
    def generate(self, field: dict, schema_name:str, field_name:str):
        raise NotImplementedError()
