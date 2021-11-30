from brownie import Bank, Token1, Token2, interface, accounts


def approveToken(amount, to, myAcc, tokenAddr):
    print(f"approving token {tokenAddr}")
    erc = interface.IERC20(tokenAddr)
    tx = erc.approve(to, amount, {"from": myAcc})
    tx.wait(1)
    return tx

def transferToken(value, recipient, sender, tokenAddr):
    print(f"transfering token {tokenAddr}")
    erc = interface.IERC20(tokenAddr)
    if erc.allowance(accounts[0], accounts[1]) >= value:
        print("tranfer allowed")
        tx = erc.transferFrom(sender, recipient, value, {"from": recipient})
        tx.wait(1)
    return tx


def main():
    bank = Bank.deploy({'from':accounts[0]})
    token1 = Token1.deploy(1000, {"from": accounts[0]})
    token2 = Token2.deploy(100, {"from": accounts[0]})
    amount1 = 50
    amount2 = 60

    bank.addToken(token1.address, {"from": accounts[0]})
    bank.addToken(token2.address, {"from": accounts[0]})

    approveToken(amount1, bank.address, accounts[0], token1.address)
    approveToken(amount2, bank.address, accounts[0], token2.address)

    print(f"allowance1 {token1.allowance(accounts[0], bank.address)}")
    print(f"allowance2 {token2.allowance(accounts[0], bank.address)}")

    bank.depositToken(token1.address, amount1, {"from": accounts[0]})
    bank.depositToken(token2.address, amount2, {"from": accounts[0]})

    print(f"balance1 of acc0 {token1.balanceOf(accounts[0])}")
    print(f"balance1 of bank {token1.balanceOf(bank.address), bank.tokenBalance(token1.address, accounts[0])}")


    print(f"balance2 of acc0 {token2.balanceOf(accounts[0])}")
    print(f"balance2 of bank {token2.balanceOf(bank.address) , bank.tokenBalance(token2.address, accounts[0])}")

    bank.withdrawToken(token1.address, amount1/2, {"from": accounts[0]})
    print(f"balance1 of acc0 {token1.balanceOf(accounts[0])}")
    print(f"balance1 of bank {token1.balanceOf(bank.address), bank.tokenBalance(token1.address, accounts[0])}")

    bank.withdrawToken(token2.address, amount2/2, {"from": accounts[0]})
    print(f"balance1 of acc0 {token2.balanceOf(accounts[0])}")
    print(f"balance1 of bank {token2.balanceOf(bank.address), bank.tokenBalance(token2.address, accounts[0])}")
