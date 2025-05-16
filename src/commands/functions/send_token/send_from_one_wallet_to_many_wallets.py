import os

from typer import Typer

from functions.send_from_one_wallet_to_many_wallets.send_from_wallet_to_wallets import (
    send_token_from_one_wallet_to_many_wallets,
)

app = Typer()


def get_wallet_config_info() -> str:
    from functions.send_from_one_wallet_to_many_wallets import config

    config_path = os.path.abspath(config.__file__)

    lines = [
        f"Send Token from one wallet to many addresses\nYou need to fill config file:\n  {config_path}\nCurrent config values:"
    ]

    for name, value in config.config.model_dump().items():
        lines.append(f"  {name} = {repr(value)}")

    return "\n".join(lines)


@app.command(
    name="from_one",
    help=get_wallet_config_info(),
)
def s_t():
    send_token_from_one_wallet_to_many_wallets()
