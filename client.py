import os
import logging
from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException

# Load environment variables
load_dotenv()


class BinanceFuturesClient:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        if not self.api_key or not self.api_secret:
            raise ValueError("Missing Binance API credentials in .env")

        try:
            self.client = Client(
                self.api_key,
                self.api_secret,
                testnet=True
            )

            self.client.API_URL = "https://testnet.binancefuture.com"

            logging.info("Binance Futures Testnet client initialized.")

        except Exception as e:
            logging.error(f"Client init failed: {str(e)}")
            raise

    def get_current_price(self, symbol: str) -> float:
        """
        Fetch current market price
        """
        ticker = self.client.futures_symbol_ticker(symbol=symbol)
        return float(ticker["price"])

    def place_order(self, params: dict) -> dict:
        try:
            logging.info(f"Sending order request: {params}")

            response = self.client.futures_create_order(**params)

            logging.info(f"Raw response: {response}")

            return {
                "orderId": response.get("orderId"),
                "status": response.get("status"),
                "executedQty": response.get("executedQty"),
                "avgPrice": response.get("avgPrice", "N/A"),
            }

        except BinanceAPIException as e:
            logging.error(f"Binance API Error: {str(e)}")
            raise Exception(f"Binance API Error: {str(e)}")

        except Exception as e:
            logging.error(f"Unexpected error: {str(e)}")
            raise Exception(f"Unexpected error: {str(e)}")