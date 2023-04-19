import click
from pysr.julia_helpers import install


@click.group("cli")
@click.pass_context
def cli():
    somevariable = "33"


@cli.command("install")
@click.option("--julia_project", default=None)
@click.option("--quiet", default=False)
@click.option("--precompile", default=None)
def _install(julia_project, quiet, precompile):
    install(julia_project, quiet, precompile)
