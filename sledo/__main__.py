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

    # check if the out directory already exists

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

    steps = config.get("steps")
    schemas = config.get("schemas")

    # go through steps
    for step in steps:
        # find schema
        schema_type = step.get("type")

        if type(schema_type) is str:
            schema = schemas.get(schema_type)
        else:
            # TODO: implement
            click.echo("Oh no!")

        keys = [
            # "id",
            *schema.keys()]

        rows = []
        columns = []

        for key in keys:
            field = schema.get(key)
            columns.append(generators.generate(field, schema_type, key))

        rows.append(columns)

        path = os.path.join(outdir, f"{schema_type}.csv")
        with open(path, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(keys)
            writer.writerows(rows)


cli.add_command(generate)

if __name__ == '__main__':
    cli()
