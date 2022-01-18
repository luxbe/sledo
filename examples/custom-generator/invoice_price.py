

from typing import Dict
from sledo.generate.field_generators import FieldGenerator, get_value_by_attr_name


class InvoicePriceGenerator(FieldGenerator):
    def generate(self, res: Dict, iter_res: Dict, **_):
        # get latest order
        amount = get_value_by_attr_name("amount", "Order", res, iter_res)
        product = get_value_by_attr_name("product", "Order", res, iter_res)

        return product["price"] * amount

    def val_to_str(self, value) -> str:
        return f"{value:.2f}"
