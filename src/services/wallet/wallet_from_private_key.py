from eth_account import Account

from services.wallet.wallet_base import WalletBase


class WalletFromPrivateKey(WalletBase):
    def __init__(self, private_key: str):
        super().__init__()
        self.private_key = private_key
        self.account = None
        self.address = None
        self.set_account()

    def set_account(self):
        self.account = Account.from_key(self.private_key)

    def get_address(self) -> str:
        if self.address is not None:
            return self.address
        self.address = self.account.address
        return self.address

    def get_private_key(self) -> str:
        return self.private_key

    def get_mnemonic(self) -> None:
        return None
