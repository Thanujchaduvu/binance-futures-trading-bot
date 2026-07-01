# Binance Futures Trading Bot

## Features

- Binance Futures Testnet
- Market Orders
- Limit Orders
- BUY & SELL
- CLI Interface
- Input Validation
- Logging
- Exception Handling

## Installation

```bash
git clone <repository>
cd trading_bot

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

python main.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001