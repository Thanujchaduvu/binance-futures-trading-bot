from bot.orders import place_limit_order

order = place_limit_order(
    symbol="BTCUSDT",
    side="BUY",
    quantity=0.001,
    price=50000
)

print(order)