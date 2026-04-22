def validate_limit_price(client, symbol, side, price):
    """
    Ensure LIMIT price makes sense relative to market
    """
    current_price = client.get_current_price(symbol)

    if side == "SELL" and price < current_price:
        raise ValueError(
            f"SELL LIMIT price must be >= current price ({current_price})"
        )

    if side == "BUY" and price > current_price:
        raise ValueError(
            f"BUY LIMIT price must be <= current price ({current_price})"
        )


def build_order_params(symbol, side, order_type, quantity, price=None):
    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    return params


def execute_order(client, symbol, side, order_type, quantity, price=None):
    """
    Full order execution flow
    """

    if order_type == "LIMIT":
        validate_limit_price(client, symbol, side, price)

    params = build_order_params(symbol, side, order_type, quantity, price)

    response = client.place_order(params)

    return response