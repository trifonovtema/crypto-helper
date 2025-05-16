import os

from typer import Typer

from functions.check_balance.check_balance import check_balance

app = Typer()


def get_wallet_config_info() -> str:
    from functions.check_balance import config

    config_path = os.path.abspath(config.__file__)

    lines = [
        f"Check balance\nYou need to fill config file:\n  {config_path}\nCurrent config values:"
    ]

    for name, value in config.config.model_dump().items():
        lines.append(f"  {name} = {repr(value)}")

    return "\n".join(lines)


@app.command(
    name="cb",
    help=get_wallet_config_info(),
)
def cb():
    check_balance()
