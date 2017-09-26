import click

@click.command()
def hello_world():
    click.echo("Hello world!")

# By adding the following, this command can be executed
# as a standalone CLI application
if __name__ == "__main__":
    hello_world()
