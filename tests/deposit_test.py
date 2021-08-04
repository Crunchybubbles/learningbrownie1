from brownie import Bank, accounts


def main():
    accounts[0].transfer(Bank[0], 1 'ether', {'from': accounts[0]} )
