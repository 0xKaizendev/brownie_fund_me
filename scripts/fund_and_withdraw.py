from webbrowser import get
from brownie import accounts, FundMe
from scripts.helpful_scripts import get_account


def fund_me():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee() * 1000
    print(entrance_fee)
    fund_me.fund({"from": account, "value": entrance_fee})


def main():
    # fund_me()
    withdraw()


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})
