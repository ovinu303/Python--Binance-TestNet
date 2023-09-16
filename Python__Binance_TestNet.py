from binance.client import Client

# Initialize the Binance client
client = Client('YOUR_API_KEY', 'YOUR_SECRET_KEY')

#Switch to the testnet
client.API_URL = 'https://testnet.binance.vision/api'

# Get account information
info = client.get_account()

# Print all balances
for asset in info['balances']:
    print(f"{asset['asset']} Balance: {asset['free']}")
