import click
from bnb_cli.main import bnb_greenfield


@click.group()
def cli():
    "support the bank functions, including transfer in greenfield and query balance"


@cli.command()
@click.option("-a", "--address", required=True, help='account address')
def balance(address):
    "query the balance of account"
    try:
        query = bnb_greenfield.query_balances(address)
        print(f"balance {query[0].get('amount')} {query[0].get('denom')}")
    except:
        print("error, address")


@cli.command()
@click.option("-ta", "-toAddress", required=True, help='account address')
def transfer(toAddress):
    "transfer to an account in Greenfield"
    print(f"{toAddress}")
