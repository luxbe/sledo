"""
This is the entry point for the "generate" module.
"""

from typing import Dict, List, Tuple

from sledo.generate.base import FieldGenerator
from sledo.generate.date import DateGenerator
from sledo.generate.number import NumberGenerator


generators: Dict[str, FieldGenerator] = {
    "number": NumberGenerator(),
    "date": DateGenerator(),
}


def generateByConfig(config: Dict) -> Dict[str, Tuple[List[str], List[List]]]:
    """Generates the data based on the configuration file

        Params:
            config (Dict): the validated configuration file

        Returns:
            data (Dict): the generated data by name and rows
    """
    res: Dict[str, Tuple[List[str], List[List]]] = {}

    amount: int = config.get("amount", 1)
    steps: Dict = config.get("steps")
    initial_step: str = config.get("initial")
    schemas: Dict = config.get("schemas")

    for _ in range(amount):

        # get initial step
        step: Dict = steps.get(initial_step)

        while step is not None:
            generateFromStep(step, schemas, res)

            step = steps.get(step.get("next"))

    return res


def generateFromStep(step: Dict, schemas: Dict, res: Dict[str, Tuple[List[str], List[List]]]):
    schema_name: str = step.get("generate")
    schema: Dict = schemas.get(schema_name)

    # initialize schema result
    if res.get(schema_name) is None:
        res[schema_name] = (["id", *schema.keys()], [])

    schema_values: List = [len(res[schema_name][1]) + 1]

    for key in schema.keys():
        field = schema.get(key)
        field_type = field if type(
            field) is str else field.get("type")
        field_options = {} if type(field) is str else field

        generator = generators.get(field_type)

        if generator is not None:
            value = generator.generate(
                field_options, schema_name, key)
        elif res.get(field_type) is not None:
            value = len(res[field_type][1])
        else:
            raise NotImplementedError()

        schema_values.append(value)

    res[schema_name][1].append(schema_values)
