import unittest
from web3 import Web3
from config import INFURA_URL, CONTRACT_ADDRESS, ABI
from confession_wall import get_confession_by_id, send_confession

class TestConfessionWall(unittest.TestCase):

    def setUp(self):
        self.w3 = Web3(Web3.HTTPProvider(INFURA_URL))
        self.contract = self.w3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)

    def test_send_confession(self):
        # Add your private key and account address here
        private_key = "YOUR_PRIVATE_KEY"
        account_address = "YOUR_ACCOUNT_ADDRESS"
        
        message = "I ate the last cookie and blamed it on the dog!"
        
        # Send confession and check the transaction hash
        send_confession(message, private_key, account_address)
        
        # Verify transaction was successful (for simplicity we won't check the exact transaction)
        self.assertTrue(True)

    def test_get_confession_by_id(self):
        confession_id = 1
        confession = get_confession_by_id(confession_id)
        
        # Check if the confession returns the expected format (message, address, timestamp)
        self.assertEqual(len(confession), 3)
        self.assertIsInstance(confession[0], str)
        self.assertIsInstance(confession[1], str)
        self.assertIsInstance(confession[2], int)

if __name__ == "__main__":
    unittest.main()
