import click


@click.command()
@click.option("--count", default=1, help="Number of Hello Worlds")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME by the world for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"Hello {name}, the world is greeting you!")


if __name__ == '__main__':
    hello()
