# Abacus Wallet Bridge
Desktop application to support [Abacus Wallet](https://github.com/Kevingislason/abacus_wallet), a DIY Bitcoin hardware wallet

## Demo
https://www.youtube.com/watch?v=G7fQn-IfNgs

## Features
- Send and receive funds on the Bitcoin testnet

- BIP39 recovery phrases

- BIP32 hierarchical deterministic key derivation

- Segwit addresses

- [Intelligent coin selection](https://github.com/Kevingislason/bitcoin_coin_selection)

## How to run (requires [microcontroller](https://www.st.com/en/evaluation-tools/32f469idiscovery.html))
1. Build [Abacus Wallet](https://github.com/Kevingislason/abacus_wallet) and put firmware on the microcontroller's volume
2. ```pipenv install```
3. ```python3 Abacus Hardware Wallet.py```

## Special thanks
Thanks to Justin Moon for getting me started programming Bitcoin

Thanks to Stepan Snigirev for his [micropython Bitcoin bundle](https://github.com/diybitcoinhardware/f469-disco), which proved invaluable
