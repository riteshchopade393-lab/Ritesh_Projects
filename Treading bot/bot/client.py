from binance.client import Client
from bot.logging_config import logger
import os

class BinanceClient:
    def __init__(self):
        self.api_key = os.getenv("I don't get api key")
        self.api_secret = os.getenv("I don't get api key secret")

        if not self.api_key or not self.api_secret:
            raise ValueError("API keys not found in environment variables")

        # Enable testnet
        self.client = Client(
            api_key=self.api_key,
            api_secret=self.api_secret,
            testnet=True
        )

        # Correct Futures Testnet URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        logger.info("Binance Futures Testnet client initialized")

    def place_order(self, **kwargs):
        try:
            logger.info(f"Placing order: {kwargs}")
            response = self.client.futures_create_order(**kwargs)
            logger.info(f"Order response: {response}")
            return response
        except Exception as e:
            logger.error(f"API Error: {e}")
            raise

