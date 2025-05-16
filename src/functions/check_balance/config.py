from pydantic import BaseModel


class Config(BaseModel):
    addresses_filename: str = "addresses_sample.txt"
    token_contract_address: str | None = None  # None if it is native token
    chain_slug: str = "bsc_testnet"  # from /src/services/chain.py


config = Config()
