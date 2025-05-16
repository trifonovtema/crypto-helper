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


def send_token():

    operation = Operation(get_chain())

    with open(get_file_path(config.source_wallets_yaml)) as f:
        source_wallet_dict = yaml.safe_load(f)
        for wallet_dict in source_wallet_dict:
            for wallet_name, wallet_params in wallet_dict.items():
                print(f"Working with wallet {wallet_name!r}")
                print(f"Wallet params: {wallet_params}")
                source_wallet = None
                if "mnemonic" in wallet_params:
                    source_wallet = Wallet(mnemonic=wallet_params["mnemonic"])
                elif "private_key" in wallet_params:
                    source_wallet = Wallet(private_key=wallet_params["private_key"])
                else:
                    raise ValueError(
                        "There should be specified mnemonik or private key for wallet"
                    )

                with open(get_file_path(config.target_addresses_filename)) as f_target:
                    target_addresses = [
                        line.strip() for line in f_target if line.strip()
                    ]
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
