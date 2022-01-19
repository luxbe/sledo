from random import randint
from sledo.generate.field_generators import FieldGenerator, DateFieldGenerator, get_schema_by_id, get_value_by_attr_name


class PaymentDateGenerator(DateFieldGenerator):
    def generate(self, schema_name, **kwargs):
        payment_status = get_value_by_attr_name(
            "status", schema_name, **kwargs)

        if payment_status == "pending":
            return None

        return super().generate(schema_name=schema_name, **kwargs)


class PaymentStatusGenerator(FieldGenerator):
    def generate(self, schema_name, res, iter_res):
        order = get_value_by_attr_name(
            "order", schema_name, res, iter_res)

        customer_id = order["customer"]
        customer = get_schema_by_id(customer_id, "Customer", res, iter_res)

        # check payment probability
        if randint(0, 100) <= customer[-1]:
            return "paid"
        else:
            return "pending"
