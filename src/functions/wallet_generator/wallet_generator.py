import os

import yaml
from rich import print
from rich.markdown import Markdown

from services.wallet.wallet import Wallet

from .config import config


def generate_wallets():
    print("Generating Wallets")
    data = []
    for i in range(1, config.wallets_number + 1):
        wallet_generator = Wallet()
        wallet_data = {
            f"{config.wallet_prefix} {i}": {
                "mnemonic": wallet_generator.get_mnemonic(),
                "address": wallet_generator.get_address(),
                "private_key": wallet_generator.get_private_key(),
            }
        }
        print(Markdown(f"# Wallet {i}"))
        for key, value in wallet_data[f"{config.wallet_prefix} {i}"].items():
            print(f"- {key}: {value!r}")
        print("\n")

        data.append(wallet_data)
    with open(f"{config.output_file_name}.yaml", "w") as file:
        print(f"Number of generated wallets: {config.wallets_number}")
        print(
            f"Filename with generated wallets: {os.path.abspath(f'{config.output_file_name}.yaml')}"
        )
        print(f"Wallets prefix: {config.wallet_prefix!r}")
        yaml.dump(data, file, default_flow_style=False, allow_unicode=True)
