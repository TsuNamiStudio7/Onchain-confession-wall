from web3 import Web3
import json
from config import INFURA_URL, CONTRACT_ADDRESS, ABI

# Set up Web3 connection
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Load contract ABI and set up contract
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)

def send_confession(message, private_key, account_address):
    # Prepare the transaction
    nonce = w3.eth.getTransactionCount(account_address)
    tx = contract.functions.confess(message).buildTransaction({
        'chainId': 1,
        'gas': 2000000,
        'gasPrice': w3.toWei('20', 'gwei'),
        'nonce': nonce,
    })

    # Sign the transaction
    signed_tx = w3.eth.account.signTransaction(tx, private_key)

    # Send the transaction
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(f"Confession sent! Transaction hash: {w3.toHex(tx_hash)}")

def get_confession_by_id(confession_id):
    confession = contract.functions.getConfession(confession_id).call()
    print(f"Confession: {confession[0]}\nOwner: {confession[1]}\nTimestamp: {confession[2]}")
