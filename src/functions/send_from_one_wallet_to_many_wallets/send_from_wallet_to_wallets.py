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


def send_token_from_one_wallet_to_many_wallets():

    operation = Operation(get_chain())

    with open(get_file_path(config.source_wallet_yaml)) as f:
        source_wallet_dict = yaml.safe_load(f)
        if "mnemonic" in source_wallet_dict:
            source_wallet = Wallet(mnemonic=source_wallet_dict["mnemonic"])
        else:
            source_wallet = Wallet(private_key=source_wallet_dict["private_key"])
        with open(get_file_path(config.target_addresses_filename)) as f_target:
            target_addresses = [line.strip() for line in f_target if line.strip()]
            for target_address in target_addresses:
                print(
                    f"[bold]Working with target address [green]{target_address!r}[/green][/bold]"
                )
                operation.send(
                    wallet=source_wallet,
                    amount=config.amount,
                    to_address=target_address,
                )
                print(
                    "-----------------------------------------------------------------"
                )
