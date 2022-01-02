from typing import Dict, Tuple, List
import os
import csv

from sledo.generate.field_generators.base import FieldGenerator
from sledo.generate.field_generators.schema import SchemaFieldGenerator

from .config import loadConfig


def main(file: str, outdir: str):
    """The main entry point for the generate command

        Params:
            file (str): the validated file path
            outdir (str): the path to the 'out'-directory, where data should be stored
    """
    config = loadConfig(file)
    data = generateByConfig(config)

    # write data to disk
    for key in data.keys():
        path = os.path.join(outdir, f"{key}.csv")

        with open(path, "w", newline='') as file:
            writer = csv.writer(file)
            schema = data.get(key)

            # write header
            writer.writerow(schema[0])
            # write content
            writer.writerows(schema[1])


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
    schemas: Dict[str, Dict[str, FieldGenerator]] = config.get("schemas")

    for _ in range(amount):

        # get initial step
        step: Dict = steps.get(initial_step)
        step_res: Dict[str, Tuple[List[str], List[List]]] = {}

        while step is not None:
            # get schema data
            schema_name: str = step.get("generate")
            schema: Dict[str, FieldGenerator] = schemas.get(schema_name)
            header = ["id", *schema.keys()]

            # initialize schema entry
            if step_res.get(schema_name) is None:
                step_res[schema_name] = (header, [])
            # initialize schema values with id
            id = 1 if res.get(schema_name) is None else len(
                res[schema_name][1]) + 1
            schema_values: List = [id]

            # generate values
            for field in schema.values():
                if isinstance(field, SchemaFieldGenerator):
                    value = field.generate(step_res)
                elif isinstance(field, FieldGenerator):
                    value = field.generate()
                else:
                    raise Exception(f"Unknown field:\n{field}")
                schema_values.append(value)

            step_res[schema_name][1].append(schema_values)

            # advance to next step
            step = steps.get(step.get("next"))

        # add step data to complete data
        for key, value in step_res.items():
            if res.get(key) is None:
                res[key] = value
            else:
                res[key][1].append(*value[1])

    return res


def generateFromStep(step: Dict, schemas: Dict, res: Dict[str, Tuple[List[str], List[List]]]):
    schema_name: str = step.get("generate")
    schema: Dict = schemas.get(schema_name)

    header = ["id", *schema.keys()]

    # initialize schema result
    if res.get(schema_name) is None:
        res[schema_name] = (header, [])

    schema_values: List = [len(res[schema_name][1]) + 1]

    res[schema_name][1].append(schema_values)
