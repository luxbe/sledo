import os
import click
from sledo.generate import main as generate_main


@click.group()
def cli():
    pass


@click.command()
@click.argument("file")
@click.option("-O", "--outdir", default="./out/", help="The out directory for the generated CSVs")
def generate(file: str, outdir: str):
    if not os.path.isfile(file):
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

    generate_main(file, outdir)


if __name__ == '__main__':
    cli.add_command(generate)
    cli()
