from random import randint
from sledo.generate.field_generators.base import FieldGenerator

values = ("Austria",
          "Belgium",
          "Bulgaria",
          "Croatia",
          "Cyprus",
          "Czech Republic",
          "Denmark",
          "Estonia",
          "Finland",
          "France",
          "Germany",
          "Greece",
          "Hungary",
          "Ireland",
          "Italy",
          "Latvia",
          "Lithuania",
          "Luxembourg",
          "Malta",
          "Netherlands",
          "Poland",
          "Portugal",
          "Romania",
          "Slovakia",
          "Slovenia",
          "Spain",
          "Sweden",
          "United States",
          "Japan",
          "United Kingdom",
          "Bangladesh",
          "Argentina",
          "China")

count = len(values) - 1


class CustomerAddressGenerator(FieldGenerator):
    def generate(self, **_):
        return values[randint(0, count)]
