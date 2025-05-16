import os

from typer import Typer

from .send_token.send_from_one_wallet_to_many_wallets import (
    app as send_from_wallet_to_wallets_app,
)
from .send_token.send_from_many_wallets_to_one_address import (
    app as send_from_many_wallets_to_one_address_app,
)

app = Typer(
    name="st",
    help="Send Token",
    no_args_is_help=True,
)


app.add_typer(send_from_wallet_to_wallets_app)
app.add_typer(send_from_many_wallets_to_one_address_app)
