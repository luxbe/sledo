import os
import csv
import click
from schema import SchemaError
from sledo.generate import generateByConfig
from sledo.load_config import loadConfig


@click.group()
def cli():
    pass


@click.command()
@click.argument("file")
@click.option("-O", "--outdir", default="./out/", help="The out directory for the generated CSVs")
def generate(file: str, outdir: str):
    # load the configuration file
    if os.path.isfile(file):
        try:
            config = loadConfig(file)
        except Exception as e:
            raise click.UsageError(e)
    else:
        raise click.UsageError(f"File does not exist: '{file}'")

    # check if the 'out'-directory already exists
    if os.path.isdir(outdir):
        # TODO: change to override check
        override = True
        # override = click.confirm(f"The directory '{outdir}' already exists. Do you want to overwrite it?", default=False, abort=False, prompt_suffix=": ", show_default=True, err=False)

        if not override:
            raise click.UsageError("Process aborted")
    # try to create the directory
    else:
        try:
            os.mkdir(outdir)
        except OSError as e:
            raise click.UsageError(e)

    generated_data = generateByConfig(config)

    # write data to disk
    for key in generated_data.keys():
        path = os.path.join(outdir, f"{key}.csv")

        with open(path, "w", newline='') as file:
            writer = csv.writer(file)
            schema = generated_data.get(key)

            # write header
            writer.writerow(schema[0])

            # write content
            writer.writerows(schema[1])


if __name__ == '__main__':
    cli.add_command(generate)
    cli()
