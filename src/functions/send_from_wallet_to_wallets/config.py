from pydantic import BaseModel


class Config(BaseModel):
    source_wallet_yaml: str = "source_wallet_sample.yaml"
    target_wallets_yaml: str = "target_wallets_sample.yaml"
    token_contract_address: str | None = None  # None if it is native token
    amount: float = 0.000001
    chain_slug: str = "bsc_testnet"  # from /src/services/chain.py


config = Config()
