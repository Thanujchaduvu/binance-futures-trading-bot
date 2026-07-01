import os
from dotenv import load_dotenv
from binance.client import Client
from bot.logging_config import logger

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_SECRET_KEY")

if not API_KEY or not API_SECRET:
    raise ValueError("API keys not found in .env")

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

logger.info("Connected to Binance Futures Testnet")
print("API Key Loaded:", API_KEY[:6] + "..." if API_KEY else "Not Found")
print("Secret Loaded:", "Yes" if API_SECRET else "No")