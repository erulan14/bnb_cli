import click


@click.group()
def cli():
    "support the payment operation functions"


@cli.command()
def create_account():
    "create-account"
    print("created")


@cli.command()
@click.option("-o", "--owner", required=True, help="owner address")
def ls(owner):
    "list payment accounts under owner or a address with optional flag --user"
    print(owner)
