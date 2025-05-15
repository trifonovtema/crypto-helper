from services.chains.base.chain import Chain
from services.chains.base.chain_registry import ChainRegistry

BSC_TEST_CHAIN = Chain(
    rpc_url="https://data-seed-prebsc-1-s1.binance.org:8545/",
    name="BNB Testnet",
    slug="bsc_testnet",
    native_token="BNB",
    scan="https://testnet.bscscan.com/",
    chain_id=97,
    contract_addresses={
        "BRIDGE(BNB->BNB Greenfield)": "0xED8e5C546F84442219A5a987EE1D820698528E04"
    },
    native_token_decimals=18,
)
BSC_CHAIN = Chain(
    rpc_url="https://bsc-dataseed.bnbchain.org/",
    name="Binance Smart Chain",
    slug="bsc",
    native_token="BNB",
    scan="https://bscscan.com/",
    chain_id=56,
    contract_addresses={
        "BRIDGE(BNB->BNB Greenfield)": "0xeA97dF87E6c7F68C9f95A69dA79E19B834823F25"
    },
    native_token_decimals=18,
)


ChainRegistry.register(BSC_TEST_CHAIN)
ChainRegistry.register(BSC_CHAIN)
