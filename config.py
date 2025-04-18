INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
CONTRACT_ADDRESS = "YOUR_CONTRACT_ADDRESS"

# ABI for the ConfessionWall contract
ABI = json.loads('[{"constant":true,"inputs":[{"name":"_id","type":"uint256"}],"name":"getConfession","outputs":[{"name":"","type":"string"},{"name":"","type":"address"},{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"_message","type":"string"}],"name":"confess","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"confessionCount","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"name":"id","type":"uint256"},{"indexed":false,"name":"message","type":"string"},{"indexed":false,"name":"owner","type":"address"},{"indexed":false,"name":"timestamp","type":"uint256"}],"name":"NewConfession","type":"event"}]')
