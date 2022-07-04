from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3

LOCAL_ENVIRONMENT_BLOCKCHAIN = ["development", "peristant-ganache"]
FORKED_LOCAL_ENVIRONMENT = ["mainnet-fork-dev", "mainnet-fork"]

decimals = 8
starting = 120000000000


def get_account():
    if (
        network.show_active() in LOCAL_ENVIRONMENT_BLOCKCHAIN
        or network.show_active() in FORKED_LOCAL_ENVIRONMENT
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"Le reseau actuel est {network.show_active()}")
    print("En cours de deploiement...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(decimals, starting, {"from": get_account()})
        print("Mock deployé ")
    else:
        print(
            f"Le contrat du priceFeed est deja disponible à {MockV3Aggregator[-1].address} "
        )
