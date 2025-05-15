import os

from bip_utils import (
    Bip39MnemonicGenerator,
    Bip39SeedGenerator,
    Bip44,
    Bip44Coins,
    Bip44Changes,
)

from services.wallet.wallet_base import WalletBase


class WalletFromMnemonic(WalletBase):
    def __init__(
        self,
        mnemonic: str = None,
        account_index: int = 0,
        change: Bip44Changes = Bip44Changes.CHAIN_EXT,
        address_index: int = 0,
    ):
        super().__init__()
        self.mnemonic = None
        self.seed_bytes = None
        self.wallet = None
        self.account = None
        self.address = None
        self.private_key = None
        self.account_index = account_index
        self.change = change
        self.address_index = address_index

        self.set_mnemonic(mnemonic)
        self.generate_seed()
        self.generate_eth_bip44_wallet()
        self.generate_account()

    def set_mnemonic(self, mnemonic: str | None = None) -> str:
        if mnemonic:
            self.mnemonic = mnemonic
            return self.mnemonic
        entropy_bytes = os.urandom(16)  # 16 байт = 128 бит
        mnemonic = Bip39MnemonicGenerator().FromEntropy(entropy_bytes)
        self.mnemonic = str(mnemonic)
        return self.mnemonic

    def generate_seed(self):
        if self.mnemonic is None:
            self.mnemonic = self.set_mnemonic()
        self.seed_bytes = Bip39SeedGenerator(self.mnemonic).Generate()
        return self.seed_bytes

    def generate_eth_bip44_wallet(self):
        if self.seed_bytes is None:
            self.seed_bytes = self.generate_seed()
        self.wallet = Bip44.FromSeed(self.seed_bytes, Bip44Coins.ETHEREUM)
        return self.wallet

    def generate_account(self):
        if self.wallet is None:
            self.wallet = self.generate_eth_bip44_wallet()
        self.account = (
            self.wallet.Purpose()
            .Coin()
            .Account(self.account_index)
            .Change(self.change)
            .AddressIndex(self.address_index)
        )
        return self.account

    def get_address(self) -> str:
        if self.address is not None:
            return self.address
        if self.account is None:
            self.account = self.generate_account()
        self.address = str(self.account.PublicKey().ToAddress())
        return self.address

    def get_private_key(self) -> str:
        if self.private_key:
            return self.private_key
        if self.account is None:
            self.account = self.generate_account()
        self.private_key = self.account.PrivateKey().Raw().ToHex()
        return self.private_key

    def get_mnemonic(self) -> str:
        if self.mnemonic is None:
            self.set_mnemonic()
        return self.mnemonic
