from bot.client import client

try:
    account = client.futures_account()

    print("✅ Connected successfully!")
    print("Available Balance:", account["availableBalance"])

except Exception as e:
    print("❌ Connection Failed")
    print(e)