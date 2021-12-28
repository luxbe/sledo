class AttributeError(Exception):
    """Base exception class for any attribute errors.

        Attributes:
            attribute -- attribute name that is missing
            schema -- the schema the attribute is missing from
            field -- the field name of the schema that the attribute is missing from
    """

    def __init__(self, attribute: str, message: str, schema: str, field: str):
        super().__init__(
            f"Attribute '{attribute}' {message} in {schema}.{field}")


class MissingAttributeError(AttributeError):
    """Exception raised for missing attributes.

    Attributes:
        attribute -- attribute name that is missing
        schema -- the schema the attribute is missing from
        field -- the field name of the schema that the attribute is missing from
    """

    def __init__(self, attribute: str, schema: str, field: str):
        super().__init__(attribute, "is required", schema, field)


class MissingSchemaError(Exception):
    """Exception raised for missing schemas.

        Attributes:
            schema -- schema name that is missing
    """

    def __init__(self, schema: str):
        super().__init__(
            f"Undefined schema '{schema}'")
