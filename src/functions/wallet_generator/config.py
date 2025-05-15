from pydantic import BaseModel

class Config(BaseModel):
    wallets_number:int = 4
    output_file_name:str = "wallets"
    wallet_prefix:str = "Wallet"


config = Config()
