import typer

from commands.functions.send_tokens import app as send_tokens_app

from .functions.wallet_generator import app as wallet_generator_app
from .functions.check_balance import app as check_balance_app

app = typer.Typer(
    no_args_is_help=True,
    rich_markup_mode="rich",
)

app.add_typer(wallet_generator_app)
app.add_typer(send_tokens_app)
app.add_typer(check_balance_app)


@app.callback()
def callback():
    """
    CLI commands for working with web3
    """
