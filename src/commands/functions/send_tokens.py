import os

from typer import Typer

from functions.send_tokens.send_tokens import (
    send_token,
)

app = Typer()


def get_wallet_config_info() -> str:
    from functions.send_tokens import config

    config_path = os.path.abspath(config.__file__)

    lines = [
        f"Send Token\nYou need to fill config file:\n  {config_path}\nCurrent config values:"
    ]

    for name, value in config.config.model_dump().items():
        lines.append(f"  {name} = {repr(value)}")

    return "\n".join(lines)


@app.command(
    name="st",
    help=get_wallet_config_info(),
)
def st():
    send_token()
