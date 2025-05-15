import typer
from .functions.wallet_generator import app as wallet_generator_app
from .functions.send_from_wallet_to_wallets import (
    app as send_from_wallet_to_wallets_app,
)

app = typer.Typer(
    no_args_is_help=True,
    rich_markup_mode="rich",
)

app.add_typer(wallet_generator_app)
app.add_typer(send_from_wallet_to_wallets_app)


@app.callback()
def callback():
    """
    CLI commands for working with web3
    """
