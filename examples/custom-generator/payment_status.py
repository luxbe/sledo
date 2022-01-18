

from sledo.generate.field_generators import FieldGenerator, get_value_by_attr_name


class PaymentStatusGenerator(FieldGenerator):
    def generate(self, res, iter_res, **_):
        delivery_status = get_value_by_attr_name(
            "status", "Delivery", res, iter_res)

        if delivery_status == "awaiting payment":
            return "pending"

        return "paid"
