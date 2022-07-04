from brownie import config, FundMe, accounts, MockV3Aggregator, network, exceptions
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_ENVIRONMENT_BLOCKCHAIN,
)
import pytest


def deploy_fund_me():
    account = get_account()
    # Passer l'adresse pour le priceFeed en parametre
    if network.show_active() not in LOCAL_ENVIRONMENT_BLOCKCHAIN:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contrat deployé à l'adresse {fund_me.address}")
    return fund_me


def only_owner():
    if network.show_active() not in LOCAL_ENVIRONMENT_BLOCKCHAIN:
        pytest.skip("Only for local testing")
    fund_me = deploy_fund_me()
    bad_account = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_account})


def main():
    deploy_fund_me()
    only_owner()
