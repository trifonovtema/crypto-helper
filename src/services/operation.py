from services.chains.base.chain import Chain
from .wallet.wallet import Wallet
from rich import print
from .abis.erc20_token import ABI as ERC20_ABI
from .abis.bnb_greenfield_bridge import ABI as BNB_GREENFIELD_BRIDGE_ABI


class Operation:
    def __init__(
        self,
        chain: Chain | None = None,
    ):
        self.chain: Chain | None = chain

    def set_chain_by_rpc(self, rpc_url: str, chain_name: str):
        self.chain = Chain(
            rpc_url=rpc_url,
            name=chain_name,
        )

    def set_chain(self, chain: Chain):
        self.chain = chain

    def print_balance(
        self,
        wallet_address: str,
        balance: float,
        token_address: str | None = None,
    ):
        print(
            f"""Balance of {wallet_address!r} for {token_address if token_address else self.chain.native_token!r} is {balance!r}""",
        )

    def get_balance_for_native_token(
        self,
        wallet_address: str,
    ) -> float:
        balance = self.chain.get_w3().eth.get_balance(wallet_address)
        res = self.from_token_units(
            balance,
            self.chain.get_native_token_decimals(),
        )
        self.print_balance(wallet_address, res)
        return res

    def sign_and_send_transaction(
        self,
        tx: dict[str, str],
        wallet: Wallet,
    ) -> str:
        w3 = self.chain.get_w3()
        signed_tx = w3.eth.account.sign_transaction(
            tx,
            wallet.get_private_key(),
        )
        tx_hash = w3.eth.send_raw_transaction(
            signed_tx.raw_transaction,
        )
        print(f"Transaction Hash: {tx_hash.hex()}")
        return tx_hash.hex()

    def get_balance_for_token(
        self,
        wallet_address: str,
        token_address: str,
    ) -> float:
        token_address = self.chain.get_w3().to_checksum_address(token_address)
        erc20_abi = ERC20_ABI

        token_contract = self.chain.w3.eth.contract(
            address=token_address,
            abi=erc20_abi,
        )
        raw_balance = token_contract.functions.balanceOf(wallet_address).call()
        decimals = token_contract.functions.decimals().call()
        formatted_balance = self.from_token_units(
            raw_balance,
            decimals,
        )
        self.print_balance(
            wallet_address,
            formatted_balance,
            token_address,
        )
        return formatted_balance

    def get_balance(
        self,
        address: str | None = None,
        token_address: str | None = None,
    ) -> float:

        wallet_address = self.chain.get_w3().to_checksum_address(address)

        if token_address is None:
            return self.get_balance_for_native_token(wallet_address)

        return self.get_balance_for_token(
            wallet_address,
            token_address,
        )

    def send_native_token(
        self,
        wallet: Wallet,
        to_address: str,
        amount: float,
        nonce: int,
        gas_price: int,
    ) -> str:
        w3 = self.chain.get_w3()
        wei_amount = w3.to_wei(amount, "ether")
        estimated_gas = w3.eth.estimate_gas(
            {
                "from": wallet.get_address(),
                "to": to_address,
                "value": wei_amount,
            }
        )
        tx = {
            "nonce": nonce,
            "to": to_address,
            "value": wei_amount,
            "gas": estimated_gas,
            "gasPrice": gas_price,
            "chainId": self.chain.chain_id,
        }

        return self.sign_and_send_transaction(
            tx,
            wallet,
        )

    @staticmethod
    def to_token_units(amount: float, decimals: int) -> int:
        """Переводит читаемое значение токена в минимальные единицы"""
        return int(amount * (10**decimals))

    @staticmethod
    def from_token_units(amount: int, decimals: int) -> float:
        """Переводит минимальные единицы токена в читаемый формат"""
        return amount / (10**decimals)

    def send_token(
        self,
        wallet: Wallet,
        to_address: str,
        amount: float,
        nonce: int,
        gas_price: int,
        token_address: str,
    ) -> str:
        w3 = self.chain.get_w3()
        abi = ERC20_ABI

        # Подключение к контракту
        contract = w3.eth.contract(address=token_address, abi=abi)

        # Узнаем decimals и пересчитываем количество
        decimals = contract.functions.decimals().call()
        amount_on_chain = self.to_token_units(
            amount,
            decimals,
        )

        estimated_gas = contract.functions.transfer(
            to_address, amount_on_chain
        ).estimate_gas(
            {
                "from": wallet.get_address(),
            },
        )

        tx = contract.functions.transfer(to_address, amount_on_chain).build_transaction(
            {
                "from": wallet.get_address(),
                "gas": estimated_gas,
                "gasPrice": gas_price,
                "nonce": nonce,
                "chainId": self.chain.chain_id,
            }
        )
        return self.sign_and_send_transaction(
            tx,
            wallet,
        )

    def send(
        self,
        wallet: Wallet,
        to_address: str,
        amount: float,
        token_address: str | None = None,
    ) -> str | None:
        print(f"Send From: {wallet.get_address()!r}")
        print(f"Send To: {to_address!r}")
        print(f"Amount: {amount!r}")
        print(f"Token: {token_address if token_address else self.chain.native_token!r}")

        w3 = self.chain.get_w3()
        nonce = w3.eth.get_transaction_count(wallet.get_address(), "pending")
        print(
            f"Nonce: {nonce}",
        )
        gas_price = w3.eth.gas_price

        if token_address is None:
            return self.send_native_token(
                wallet=wallet,
                to_address=to_address,
                amount=amount,
                nonce=nonce,
                gas_price=gas_price,
            )

        return self.send_token(
            wallet=wallet,
            to_address=to_address,
            amount=amount,
            nonce=nonce,
            gas_price=gas_price,
            token_address=token_address,
        )

    def bridge_native_tokens_from_bnb_to_bnbgreenfield(
        self,
        wallet: Wallet,
        amount: float,
    ):
        contract_name = "BRIDGE(BNB->BNB Greenfield)"

        w3 = self.chain.get_w3()
        abi = BNB_GREENFIELD_BRIDGE_ABI

        # Подключение к контракту
        bridge_contract_address = self.chain.get_contract_address(
            contract_name,
        )
        contract = w3.eth.contract(address=bridge_contract_address, abi=abi)
        gas_price = w3.eth.gas_price
        nonce = w3.eth.get_transaction_count(wallet.get_address(), "pending")
        wei_amount = w3.to_wei(amount, "ether")
        wei_relay_fee = w3.to_wei(0.0006, "ether")
        wei_ack_relay_fee = w3.to_wei(0.0004, "ether")

        total_value = wei_amount + wei_relay_fee + wei_ack_relay_fee
        estimated_gas = contract.functions.transferOut(
            wallet.get_address(), wei_amount
        ).estimate_gas(
            {
                "from": wallet.get_address(),
                "value": total_value,
            }
        )

        # Собираем транзакцию
        tx = contract.functions.transferOut(
            wallet.get_address(), wei_amount
        ).build_transaction(
            {
                "from": wallet.get_address(),
                "value": total_value,
                "gas": estimated_gas,
                "gasPrice": gas_price,
                "nonce": nonce,
                "chainId": self.chain.chain_id,
            }
        )
        print(f"{tx=}")

        return self.sign_and_send_transaction(
            tx,
            wallet,
        )
