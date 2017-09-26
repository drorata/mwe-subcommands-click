import click


@click.command()
def bar():
    click.echo("running `bar` from group1/commands.py")
