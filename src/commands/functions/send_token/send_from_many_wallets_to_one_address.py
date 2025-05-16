import os

from typer import Typer

from functions.send_from_many_wallets_to_one_wallet.send_from_many_wallets_to_one_wallet import (
    send_token_from_many_wallets_to_one_address,
)

app = Typer()


def get_wallet_config_info() -> str:
    from functions.send_from_many_wallets_to_one_wallet import config

    config_path = os.path.abspath(config.__file__)

    lines = [
        f"Send Token from many wallets to one address\nYou need to fill config file:\n  {config_path}\nCurrent config values:"
    ]

    for name, value in config.config.model_dump().items():
        lines.append(f"  {name} = {repr(value)}")

    return "\n".join(lines)


@app.command(
    name="from_many",
    help=get_wallet_config_info(),
)
def s_t():
    send_token_from_many_wallets_to_one_address()
