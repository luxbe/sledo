

import csv
from sledo.generate.field_generators import DateFieldGenerator, get_value_by_attr_name


class PaymentDateGenerator(DateFieldGenerator):
    def generate(self, schema_name, **kwargs):
        payment_status = get_value_by_attr_name(
            "status", schema_name, **kwargs)

        if payment_status == "pending":
            return None

        return super().generate(schema_name=schema_name, **kwargs)
