from bip_utils import Bip44Changes

from services.wallet.wallet_base import WalletBase
from services.wallet.wallet_from_mnemonic import WalletFromMnemonic
from services.wallet.wallet_from_private_key import WalletFromPrivateKey


class Wallet(WalletBase):

    def __init__(
        self,
        mnemonic: str | None = None,
        private_key: str | None = None,
        account_index: int = 0,
        change: Bip44Changes = Bip44Changes.CHAIN_EXT,
        address_index: int = 0,
    ):
        super().__init__()
        self.impl: WalletBase | None = None
        if mnemonic and private_key:
            raise ValueError("Specify only mnemonic or privet_key. Not both of them")

        if mnemonic:
            self.impl = WalletFromMnemonic(
                mnemonic=mnemonic,
                account_index=account_index,
                change=change,
                address_index=address_index,
            )
        elif private_key:
            self.impl = WalletFromPrivateKey(private_key)
        else:
            self.impl = WalletFromMnemonic()

    def get_address(self) -> str | None:
        if self.impl is None:
            raise ValueError("Wallet is not initialized")
        return self.impl.get_address()

    def get_private_key(self) -> str | None:
        if self.impl is None:
            raise ValueError("Wallet is not initialized")
        return self.impl.get_private_key()

    def get_mnemonic(self) -> str | None:
        if self.impl is None:
            raise ValueError("Wallet is not initialized")
        return self.impl.get_mnemonic()
