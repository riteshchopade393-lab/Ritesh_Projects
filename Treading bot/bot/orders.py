from bot.client import BinanceClient
from bot.validators import validate_inputs

class OrderService:
    def __init__(self):
        self.client = BinanceClient()

    def create_order(self, symbol, side, order_type, quantity, price=None):
        validate_inputs(symbol, side, order_type, quantity, price)

        order_params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            order_params["price"] = price
            order_params["timeInForce"] = "GTC"

        return self.client.place_order(**order_params)
