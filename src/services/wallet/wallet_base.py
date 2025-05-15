from abc import ABC, abstractmethod


class WalletBase(ABC):
    def __init__(self):
        self.address = None
        self.mnemonic = None
        self.private_key = None

    @abstractmethod
    def get_address(self) -> str: ...

    @abstractmethod
    def get_private_key(self) -> str: ...

    @abstractmethod
    def get_mnemonic(self) -> str | None: ...
