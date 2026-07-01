import typer

from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)

app = typer.Typer()


def print_summary(order):
    print("\n========== ORDER SUMMARY ==========")
    print(f"Order ID      : {order['orderId']}")
    print(f"Symbol        : {order['symbol']}")
    print(f"Status        : {order['status']}")
    print(f"Side          : {order['side']}")
    print(f"Type          : {order['type']}")
    print(f"Quantity      : {order['origQty']}")
    print(f"Executed Qty  : {order['executedQty']}")
    print("===================================")


@app.command()
def order(
    symbol: str = typer.Option(..., "--symbol", help="Trading Symbol"),
    side: str = typer.Option(..., "--side", help="BUY or SELL"),
    order_type: str = typer.Option(..., "--order-type", help="MARKET or LIMIT"),
    quantity: float = typer.Option(..., "--quantity"),
    price: float = typer.Option(None, "--price"),
):
    try:
        validate_symbol(symbol)
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)

        if order_type.upper() == "MARKET":
            result = place_market_order(symbol, side.upper(), quantity)
        else:
            validate_price(price)
            result = place_limit_order(
                symbol,
                side.upper(),
                quantity,
                price,
            )

        print_summary(result)

    except Exception as e:
        typer.echo(f"❌ {e}")


if __name__ == "__main__":
    app()