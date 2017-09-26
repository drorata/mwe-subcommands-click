import click

from group1 import commands as group1
from group2 import commands as group2
from hello_world import hello_world

@click.group()
def entry_point():
    pass

entry_point.add_command(group1.bar)
entry_point.add_command(group2.foo)
entry_point.add_command(hello_world)

if __name__ == "__main__":
    entry_point()
