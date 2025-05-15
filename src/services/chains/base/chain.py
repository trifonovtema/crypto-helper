from web3 import Web3


class Chain:
    def __init__(
        self,
        rpc_url: str | None = None,
        name: str | None = None,
        native_token: str | None = None,
        scan: str | None = None,
        chain_id: int | None = None,
        contract_addresses: dict[str, str] | None = None,
        native_token_decimals: int | None = None,
        slug: str | None = None,
    ):
        self.rpc_url = rpc_url
        self.name = name
        self.native_token = native_token
        self.scan = scan
        self.chain_id = chain_id
        self.contract_address = contract_addresses
        self.w3: Web3 | None = None
        self.native_token_decimals = native_token_decimals
        self.slug = slug
        self.set_w3()

    def get_w3(self):
        if self.w3 is None:
            self.set_w3()
        return self.w3

    def set_rpc(self, rpc_url: str) -> None:
        self.rpc_url = rpc_url

    def set_w3(self) -> None:
        if self.rpc_url is None:
            raise ValueError("RPC URL is not set")
        self.w3 = Web3(Web3.HTTPProvider(self.rpc_url))

    def get_contract_address(self, name: str) -> str:
        return self.contract_address[name]

    def get_native_token_decimals(self) -> int:
        return self.native_token_decimals
