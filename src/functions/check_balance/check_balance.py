import os

import yaml
from rich import print
from rich.markdown import Markdown

from services.chains.base.chain import Chain
from services.chains.chains import ChainRegistry
from services.operation import Operation
from services.wallet.wallet import Wallet

from .config import config


def get_file_path(file_name):
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        file_name,
    )


def get_chain() -> Chain:
    chain = ChainRegistry.get(config.chain_slug)
    print(Markdown(f"# You are using {chain.name} chain"))
    return chain


def check_balance():
    operation = Operation(get_chain())
    with open(get_file_path(config.addresses_filename)) as f_target:
        addresses = [line.strip() for line in f_target if line.strip()]
        for address in addresses:
            print(f"[bold]Working with address [green]{address!r}[/green][/bold]")
            balance = operation.get_balance(
                address=address,
                token_address=config.token_contract_address,
            )
