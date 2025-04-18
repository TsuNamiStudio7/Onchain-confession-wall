from web3 import Web3

def get_account_balance(account_address, w3):
    balance_wei = w3.eth.get_balance(account_address)
    balance_eth = Web3.fromWei(balance_wei, 'ether')
    return balance_eth
