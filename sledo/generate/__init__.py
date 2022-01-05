from random import random
from types import FunctionType
from typing import Any, Dict, Tuple, List
import os
import csv

from .field_generators.base import FieldGenerator
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


def generateByConfig(config: Dict) -> Dict[str, Tuple[Tuple[str], List[List]]]:
    """Generates the data based on the configuration file

        Params:
            config (Dict): the validated configuration file

        Returns:
            data (Dict): the generated data by name and rows
    """

    res: Dict[str, Tuple[Tuple, List[List]]] = {}

    iter_amount: int = config.get("amount", 1)
    steps: Dict = config.get("steps")
    initial_step: str = config.get("initial")
    schemas: Dict[str, Dict[str, FieldGenerator]] = config.get("schemas")

    for _ in range(iter_amount):

        # get initial step
        step: Dict = steps.get(initial_step)
        iter_res: Dict[str, Tuple[Tuple,
                                  List[List[Tuple[Any, FunctionType]]]]] = {}

        while step is not None:
            # get schema data
            generate: str | Dict = step.get("generate")

            if type(generate) is str:
                schema_name = generate
            else:
                rand = random()
                total = 0
                schema_name = None

                for (key, value) in generate.items():
                    if (value + total) >= rand:
                        schema_name = key
                        break
                    total += value

            if schema_name is None:
                step = steps.get(step.get("next"))
                continue

            schema: Dict[str, FieldGenerator] = schemas.get(schema_name)
            header = ("id", *schema.keys())

            # initialize schema entry
            if iter_res.get(schema_name) is None:
                iter_res[schema_name] = (header, [])
            # initialize schema values with id
            id = 1 if res.get(schema_name) is None else len(
                res[schema_name][1]) + 1
            schema_values: List[Tuple[Any, FunctionType]] = [(id, str)]

            # generate values
            for field in schema.values():
                if isinstance(field, FieldGenerator):
                    value = field.generate(iter_res)
                    schema_values.append((value, field.val_to_str))
                else:
                    raise Exception(f"Unknown field:\n{field}")

            iter_res[schema_name][1].append(schema_values)

            # advance to next step
            step = steps.get(step.get("next"))

        # add iteration data to complete data
        for key, value in iter_res.items():
            if res.get(key) is None:
                res[key] = (value[0], [list(
                    map(lambda gen: gen[1](gen[0]), *value[1]))])
            else:
                res[key][1].append(map(lambda gen: gen[1](gen[0]), *value[1]))

    return res
