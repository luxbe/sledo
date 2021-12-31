"""
This is the "load_config" module.

The load config helps to load and validate the sledo configuration files.
"""

import click
from schema import Or, Schema, Use, Optional, SchemaError
from typing import Dict
import yaml

# The schema of a valid configuration file
schema = Schema({
    'initial': str,
    'amount': int,
    'steps': {
        str: {
            'generate': str,
            Optional('next'): str
        }
    },
    'schemas': {
        str: {
            str: Or(str, {
                'type': str,
                Optional(str): object
            })
        }
    }
})


def validateConfig(config: Dict):
    schema.validate(config)

    # TODO: validate inital_step exists
    # if step == None: raise MissingStepError(initial_step)
    # TODO: validate schemas exist
    # TODO: validate type exist
    # TODO: validate fields


def loadConfig(file: str) -> Dict:
    """
    Loads the configuration file and validates its contents

        Params:
            file (str): the file path of the configuration file

        Returns:
            config (Dict): the loaded configuration file
    """

    # load and parse the configuration file
    with open(file) as f:
        config: Dict = yaml.load(f, Loader=yaml.FullLoader)

        # validate the loaded configuration file
        validateConfig(config)

        return config
