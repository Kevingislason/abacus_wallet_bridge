import configparser
from os import path
from typing import Any


class Field:
    BLOCKCHAIN_CLIENT = "Blockchain client"
    NETWORK = "Network"
    BALANCE_UNITS = "Balance units"


class BlockchainClient:
    BLOCK_EXPLORER = "Block explorer"
    BITCOIN_NODE = "Bitcoin node"


# Required by python-bitcointx, see
# https://github.com/Simplexum/python-bitcointx#selecting-the-chain-to-use
class Network:
    REGTEST = "bitcoin/regtest"
    TESTNET = "bitcoin/testnet"
    MAINNET = "bitcoin"


class BalanceUnits:
    SATOSHIS = "satoshis"
    BTC = "BTC"


class Config:
    PATH = "config.ini"

    @classmethod
    def exists(cls):
        return path.exists(cls.PATH)

    @classmethod
    def set_defaults(cls):
        config = configparser.ConfigParser()
        config.add_section("Config")

        config.set("Config", str(Field.BALANCE_UNITS), str(BalanceUnits.BTC))
        config.set("Config", str(Field.NETWORK),
                   str(Network.TESTNET))
        config.set("Config", str(Field.BLOCKCHAIN_CLIENT),
                   str(BlockchainClient.BLOCK_EXPLORER))

        with open(cls.PATH, 'w+') as configfile:
            config.write(configfile)

    @classmethod
    def get(cls, field: Field) -> Any:
        config = configparser.ConfigParser()
        config.read(cls.PATH)
        return config["Config"][field]

    @classmethod
    def set(cls, field: Field, value: Any):
        config = configparser.ConfigParser()
        config[field] = value
        with open(cls.PATH, "w+") as configfile:
            config.write(configfile)
        configfile.close()

    @classmethod
    def get_blockchain_client(cls) -> BlockchainClient:
        return cls.get(Field.BLOCKCHAIN_CLIENT)

    @classmethod
    def set_blockchain_client(cls, blockchain_client: BlockchainClient):
        cls.set(Field.BLOCKCHAIN_CLIENT, blockchain_client)

    @classmethod
    def get_network(cls) -> Network:
        return cls.get(Field.NETWORK)

    @classmethod
    def set_network(cls, network: Network):
        cls.set(Field.Network, network)

    @classmethod
    def get_balance_units(cls) -> BalanceUnits:
        return cls.get(Field.BALANCE_UNITS)

    @classmethod
    def set_balance_units(cls, balance_display_units: BalanceUnits):
        cls.set(Field.BALANCE_UNITS, balance_display_units)
