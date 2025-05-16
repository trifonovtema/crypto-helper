from pydantic import BaseModel


class Config(BaseModel):
    source_wallets_yaml: str = "source_wallets_sample.yaml"
    target_addresses_filename: str = "target_addresses_sample.txt"
    token_contract_address: str | None = None  # None if it is native token
    amount: float = 0.000001
    chain_slug: str = "bsc_testnet"  # from /src/services/chain.py


config = Config()
