import os

from typer import Typer

from functions.wallet_generator.wallet_generator import generate_wallets

app = Typer()


def get_wallet_config_info() -> str:
    from functions.wallet_generator import config

    config_path = os.path.abspath(config.__file__)

    lines = [
        f"Generate Wallet\nYou need to fill config file:\n  {config_path}\nCurrent config values:"
    ]

    for name, value in config.config.model_dump().items():
        lines.append(f"  {name} = {repr(value)}")

    return "\n".join(lines)


@app.command(
    name="gw",
    help=get_wallet_config_info(),
)
def gw():
    generate_wallets()
