

from random import randint
from sledo.generate.field_generators import FieldGenerator, get_value_by_attr_name

values = ("awaiting payment", "sent out",
          "successful delivery", "not deliverable")
count = len(values) - 1


class DeliveryStatusGenerator(FieldGenerator):
    def generate(self, **_):

        return values[randint(0, count)]
