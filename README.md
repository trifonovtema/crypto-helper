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

uv run src/main.py
```

## ✨ Key Features

* **Check balance** — for specified addresses for native tokens and erc20 tokens.
* **Wallet Generator** — generate multiple wallets with mnemonic or private key.
* **Token Transfers** — send tokens from a single or multiple wallets to single or multiple targets.
* **Greenfield Bridge Support** — interact with BNB Greenfield Bridge contracts.
* **Modular CLI** — easily extend with new commands.

## 📄 License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE.md) file for more details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to open an issue or submit a pull request.

---

Made with ❤️ by [@trifonovtema](https://github.com/trifonovtema)
