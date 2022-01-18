

from typing import Dict
from sledo.generate.field_generators import FieldGenerator, to_ref, get_value_by_attr_name
from schema import Schema, And, Use, Or


class DiscountGenerator(FieldGenerator):
    option_schema = Schema({
        "percentage": Or(Use(to_ref), And(Use(float), lambda x: 0 <= x <= 100)),
        "timeframe": Or(Use(to_ref), And(Use(int), lambda x: 0 <= x)),
        "amount": Or(Use(to_ref), Use(float))
    })

    def validate(self):
        self.options = self.option_schema.validate(self.options)

    def generate(self, schema_name: str, res: Dict, iter_res: Dict):
        self.prepare_options(schema_name, res, iter_res)
        # get latest order
        amount = self.options["amount"]
        percentage = self.options["percentage"]
        timeframe = self.options["timeframe"]

        order_date = get_value_by_attr_name("date", "Order", res, iter_res)
        payment_date = get_value_by_attr_name(
            "date", schema_name, res, iter_res)

        return amount * (percentage / 100) if payment_date is not None and (payment_date - order_date).days <= timeframe else 0

    def val_to_str(self, value) -> str:
        return f"{value:.2f}"
