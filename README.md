# 🛡️ Crypto Helper

**Crypto Helper** is a Python utility designed to simplify cryptographic operations such as wallet generation, token transfers, and blockchain interaction. It provides a CLI interface and modular architecture for managing wallets, interacting with smart contracts, and transferring tokens across addresses or chains. The project uses a modern Python layout (`src/` structure) and is managed via [uv](https://github.com/astral-sh/uv).

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/trifonovtema/crypto-helper.git
   cd crypto-helper
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   uv venv
   uv sync
   ```

   > 💡 If `uv` is not installed, follow to [UV installation guide](https://docs.astral.sh/uv/getting-started/installation/)

## 🚀 Usage

After activating the virtual environment, run the CLI:

```bash
source .venv/bin/activate  # Unix/Linux
.venv\Scripts\activate.bat  # Windows

python src/main.py
```

## 🗂️ Project Structure

```
crypto-helper/
├── pyproject.toml                  # Project metadata and dependencies
├── uv.lock                         # Dependency lock file
├── .python-version                 # Python version used by pyenv
├── .gitignore                      # Git ignore file
├── src/
│   ├── main.py                     # Entrypoint script
│   ├── commands/                   # CLI command definitions
│   │   ├── cli.py                  # Argument parser and dispatcher
│   │   ├── send_from_wallet_to_wallets.py
│   │   ├── wallet_generator.py
│   │   └── __init__.py
│   ├── functions/                  # Business logic grouped by domain
│   │   ├── send_from_wallet_to_wallets/
│   │   │   ├── send_from_wallet_to_wallets.py
│   │   │   ├── config.py
│   │   │   ├── source_wallet_sample.yaml
│   │   │   ├── target_wallets_sample.yaml
│   │   │   └── __init__.py
│   │   ├── wallet_generator/
│   │   │   ├── wallet_generator.py
│   │   │   ├── config.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── services/                   # Blockchain logic and low-level integrations
│   │   ├── operation.py            # Execution of higher-level flows
│   │   ├── abis/                   # Contract ABI interfaces
│   │   │   ├── bnb_greenfield_bridge.py
│   │   │   ├── erc20_token.py
│   │   │   └── __init__.py
│   │   ├── chains/                 # Blockchain chain definitions
│   │   │   ├── chains.py
│   │   │   ├── base/
│   │   │   │   ├── chain.py
│   │   │   │   ├── chain_registry.py
│   │   │   │   └── __init__.py
│   │   │   └── __init__.py
│   │   ├── wallet/                 # Wallet creation and abstraction logic
│   │   │   ├── wallet.py
│   │   │   ├── wallet_base.py
│   │   │   ├── wallet_from_mnemonic.py
│   │   │   ├── wallet_from_private_key.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   └── __init__.py
```

## ✨ Key Features

* **Wallet Generator** — generate multiple wallets with mnemonic or private key.
* **Token Transfers** — send tokens from a single wallet to multiple targets.
* **Greenfield Bridge Support** — interact with BNB Greenfield Bridge contracts.
* **ERC20 Utilities** — send and manage ERC20 tokens via contract interaction.
* **Modular CLI** — easily extend with new commands.

## 📄 License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE.md) file for more details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to open an issue or submit a pull request.

---

Made with ❤️ by [@trifonovtema](https://github.com/trifonovtema)
