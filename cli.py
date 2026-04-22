import argparse
import logging

from bot.client import BinanceFuturesClient
from bot.orders import execute_order
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)
from bot.strategy import get_signal

# Logging setup
logging.basicConfig(
    filename="trading_bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    # ✅ REQUIRED inputs
    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")

    # ✅ OPTIONAL inputs
    parser.add_argument("--side", required=False, help="BUY or SELL")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT)")
    parser.add_argument("--auto", action="store_true", help="Use dataset for decision")

    args = parser.parse_args()

    try:
        # ✅ Validate core inputs
        symbol = validate_symbol(args.symbol)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)
        if args.auto:
            side = get_signal(
                "fear_greed_index.csv",
                "historical_data.csv"
                )
            print(f"\n📊 Signal from dataset: {side}")


        else:
            if not args.side:
                raise ValueError("You must provide --side when not using --auto")

            side = validate_side(args.side)

        # ✅ Initialize client
        client = BinanceFuturesClient()

        # ✅ Print summary
        print("\n=== ORDER SUMMARY ===")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        if order_type == "LIMIT":
            print(f"Price: {price}")

        # ✅ Execute order
        response = execute_order(
            client,
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        # ✅ Print response
        print("\n=== RESPONSE ===")
        print(f"Order ID: {response['orderId']}")
        print(f"Status: {response['status']}")
        print(f"Executed Qty: {response['executedQty']}")
        print(f"Avg Price: {response['avgPrice']}")

        print("\n✅ Order placed successfully!")

    except Exception as e:
        logging.error(str(e))
        print(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    main()