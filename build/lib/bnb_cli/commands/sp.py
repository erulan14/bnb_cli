from bnb_cli.main import bnb_greenfield
import click

@click.group()
def cli():
    "support the storage provider operation functions"


@cli.command()
def ls():
    "list storage providers"
    bnb_greenfield.query


@cli.command()
@click.argument("link", required=True)
def head(link):
    "get storage provider info"
    print(link)


@cli.command()
@click.argument("link", required=True)
def get_price(link):
    "get quota and storage price of storage provider"
    print(link)

