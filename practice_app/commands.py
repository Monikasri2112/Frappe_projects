import click

@click.command("hello")
def hello():
    """Print a greeting message."""
    click.echo("Hello from the custom Bench CLI!")

commands = [
    hello
]
