

from random import random
from sledo.generate.field_generators import FieldGenerator, get_schema_by_id, get_value_by_attr_name


eu_countries = ("Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary",
                "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia", "Spain", "Sweden")


class DeliveryStatusGenerator(FieldGenerator):
    def generate(self, schema_name, res, iter_res):
        payment_status = get_value_by_attr_name(
            "status", "Payment", res, iter_res)

        order = get_value_by_attr_name(
            "order", schema_name, res, iter_res)

        customer_id = order["customer"]
        address = get_value_by_attr_name(
            "address", "Customer", res, iter_res, id=customer_id)

        # check if address is outside of the eu
        if address not in eu_countries:
            return "not deliverable"

        if payment_status == "paid":
            rand = random()
            if rand <= 0.3:
                return "sent out"
            return "successful delivery"
        else:
            return "awaiting payment"
