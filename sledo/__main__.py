from typing import Dict, List, Tuple
import click
import os
import csv
from sledo import generators
from sledo.load_config import loadConfig


@click.group()
def cli():
    pass


@click.command()
@click.argument("file")
@click.option("-O", "--outdir", default="./out/", help="The out directory for the generated CSVs")
def generate(file: str, outdir: str):
    """Generates CSVs based on the given configuration file."""
    click.echo(f"Config file: {file}\nOut directory: {outdir}")
    # load the configuration file
    config = loadConfig(file)

    # check if the 'out'-directory already exists
    if os.path.isdir(outdir):
        # TODO: change to override check
        override = True
        # override = click.confirm(f"The directory '{outdir}' already exists. Do you want to override it?", default=False, abort=False, prompt_suffix=": ", show_default=True, err=False)

        if not override:
            click.echo("Process aborted")
            exit(1)
    # try to create the directory
    else:
        try:
            os.mkdir(outdir)
        except OSError as e:
            click.UsageError(e).show()
            exit(1)

    initial: str = config.get("initial")
    amount: int = config.get("amount")
    steps: Dict = config.get("steps")
    schemas: Dict = config.get("schemas")

    # The data that should be written into the CSV-files later
    csv_data: Dict[str, List[List]] = {}

    for _ in range(amount):

        # start with initial step
        step: Dict | None = steps.get(initial)
        prev: Tuple[str, List] = None

        if step == None:
            click.ClickException(f"Unknown initial step '{step}'").show()
            exit(1)

        while step is not None:
            # generates the schema from one step
            (name, row) = generateSchemaFromStep(step, schemas, prev)

            if csv_data.get(name) is None:
                csv_data[name] = []

            data_entry = csv_data.get(name)
            row_with_id = [len(data_entry)+1, *row]

            data_entry.append(row_with_id)

            prev = (name, row_with_id)
            step = steps.get(step.get("next"))

    # write data to disk
    for name in csv_data.keys():
        path = os.path.join(outdir, f"{name}.csv")

        with open(path, "w", newline='') as file:
            writer = csv.writer(file)
            # TODO: write headers
            writer.writerow(["id", *schemas.get(name).keys()])

            # write rows
            writer.writerows(csv_data.get(name))


def generateSchemaFromStep(step: Dict, schemas: Dict, prev: Tuple[str, List]) -> Tuple[str, List]:
    # find schema
    schema_name = step.get("generate")
    schema: Dict | None = schemas.get(schema_name)

    if schema is None:
        click.UsageError(f"Undefined schema '{schema_name}'").show()
        exit(1)

    def generateAttribute(key: str):
        res = generators.generate(
            schema.get(key),
            schema_name,
            key)

        if res is not None:
            return res

        if (prev is None) or (prev[0] != schema.get(key)):
            click.UsageError(f"Type '{prev[0]}' is not defined!").show()
            exit(1)

        return prev[1][0]

    # generate schema
    return (schema_name, map(generateAttribute, schema.keys()))


cli.add_command(generate)

if __name__ == '__main__':
    cli()
