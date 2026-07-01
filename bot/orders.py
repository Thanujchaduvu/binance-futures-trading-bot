# bot/orders.py

from binance.exceptions import BinanceAPIException

from bot.client import client
from bot.logging_config import logger


def place_market_order(symbol, side, quantity):
    """
    Place a MARKET order.
    """

    try:

        logger.info(
            f"MARKET ORDER REQUEST | Symbol={symbol} Side={side} Quantity={quantity}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity,
        )

        logger.info(f"MARKET ORDER SUCCESS | {order}")

        return order

    except BinanceAPIException as e:

        logger.error(f"MARKET ORDER FAILED | {e}")

        raise

    except Exception as e:

        logger.error(f"Unexpected Error | {e}")

        raise


def place_limit_order(symbol, side, quantity, price):
    """
    Place a LIMIT order.
    """

    try:

        logger.info(
            f"LIMIT ORDER REQUEST | Symbol={symbol} Side={side} Quantity={quantity} Price={price}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC",
        )

        logger.info(f"LIMIT ORDER SUCCESS | {order}")

        return order

    except BinanceAPIException as e:

        logger.error(f"LIMIT ORDER FAILED | {e}")

        raise

    except Exception as e:

        logger.error(f"Unexpected Error | {e}")

        raise