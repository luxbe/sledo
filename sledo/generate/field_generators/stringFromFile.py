from typing import Any, DefaultDict
from schema import Or, Schema, Use, Optional
import random

from .reference import to_ref
from .base import FieldGenerator
import numpy as np


class StringFieldGenerator(FieldGenerator):
    option_schema = Schema({
        "source": Or(Use(to_ref), Use(str)),
        # Optional("source", default=None): Use(str)
        "reuse": Or(Use(to_ref), Use(bool))
    })

    def validate(self):
        self.options = self.option_schema.validate(self.options)

    def generate(self, res={}):
        options = self.prepare_options(res)

        source: str = options["source"],
        reuse: bool = options["reuse"],

        # dict_no_duplicates = {}

        with open(source) as textFile:
            arr_no_duplicates = np.loadtxt(textFile, delimiter="\r\n")

        # if reuse == True:
            lines = open(source).read().splitlines()
            return random.choice(lines)

        # if reuse == False:

        #     # for i in source:
        #     # dict_no_duplicates[source].append(
        #     #   open(source).read().splitlines())
        #     # print(dict_no_duplicates)

        #     unique_element = arr_no_duplicates.pop(1)
        #     return(unique_element)

        #     # dict = {source: open(source).read().splitlines()}

        #     # fileObject = open(source, "r"),
        #     # for line in fileObject:
        #     #     element = line.split(),
        #     #     dict[element[0]] = element[1],
        #     # fileObject.close()
        #     # return dict
