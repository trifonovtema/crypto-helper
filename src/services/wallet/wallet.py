from services.wallet.wallet_base import WalletBase
from services.wallet.wallet_from_mnemonic import WalletFromMnemonic
from services.wallet.wallet_from_private_key import WalletFromPrivateKey
from bip_utils import Bip44Changes


class Wallet(WalletBase):

    def __init__(
        self,
        mnemonic: str = None,
        private_key: str = None,
        account_index: int = 0,
        change: Bip44Changes = Bip44Changes.CHAIN_EXT,
        address_index: int = 0,
    ):
        super().__init__()
        if mnemonic and private_key:
            raise ValueError("Укажи только mnemonic или private_key, не оба")

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

    def get_address(self) -> str:
        return self.impl.get_address()

    def get_private_key(self) -> str:
        return self.impl.get_private_key()

    def get_mnemonic(self) -> str | None:
        return self.impl.get_mnemonic()
