def validate_symbol(symbol: str) -> str:
    if not symbol:
        raise ValueError("Symbol cannot be empty")

    symbol = symbol.upper()  # normalize input

    if not symbol.endswith("USDT"):
        raise ValueError("Invalid symbol. Example: BTCUSDT")

    return symbol


def validate_side(side: str) -> str:
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    return side


def validate_order_type(order_type: str) -> str:
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")
    return order_type


def validate_quantity(quantity: float) -> float:
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")
    return quantity


def validate_price(price, order_type: str):
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders")
        if float(price) <= 0:
            raise ValueError("Price must be greater than 0")
        return float(price)
    return None