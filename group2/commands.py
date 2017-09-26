import click


@click.command()
def foo():
    click.echo("running `foo` from group2/commands")
