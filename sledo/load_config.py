"""
This is the "load_config" module.

The load config helps to load and validate the sledo configuration files.
"""

from schema import Or, Schema, Use, Optional, SchemaError
from typing import Dict
import yaml

# The schema of a valid configuration file
schema = Schema({
    'steps': [{
        'type': Or(str, [{
            str: lambda n: 0 <= n <= 1
        }]),
        Optional('amount'): Use(int)
    }],
    'schemas': {
        str: {
            str: Or(str, {
                'type': str,
                str: object
            })
        }
    }
})


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
    try:
        schema.validate(config)
        return config
    except SchemaError as e:
        print("Config validation error:", e)
        exit(1)
