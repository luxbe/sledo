import os
import shutil
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
        click.confirm(f"The output directory '{outdir}' and ALL ITS CONTENTS will be REMOVED! Continue?",
                      default=False, abort=True, prompt_suffix=": ", show_default=True, err=False)

        shutil.rmtree(outdir)
    # create the directory
    try:
        os.mkdir(outdir)
    except OSError as e:
        raise click.UsageError(e)

    generate_main(file, outdir)


if __name__ == '__main__':
    cli.add_command(generate)
    cli()
