Binance Futures Trading Bot (CLI-Based)

This is a command-line trading bot that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M). It also supports data-driven trading using Fear and Greed Index and historical price data.

Features

1. Place MARKET and LIMIT orders
2. Supports BUY and SELL
3. Works with Binance Futures Testnet
4. Takes input from CLI using argparse
5. Uses dataset-based trading logic
6. Performs data preprocessing
7. Uses Simple Moving Average (SMA)
8. Logs API requests and responses
9. Handles errors and exceptions

Strategy Logic

1. The bot uses two datasets
2. Fear and Greed Index is used to understand market sentiment
3. Historical price data is used to calculate SMA (10-period)
4. BUY when sentiment is low and price is above SMA
5. SELL when sentiment is high and price is below SMA
6. Fallback ensures a trade is always executed

Project Structure

trading_bot/
  bot/
    __init__.py
    client.py        # Binance client wrapper
    orders.py        # order placement logic
    validators.py    # input validation
    logging_config.py
  cli.py             # CLI entry point
  README.md
  requirements.txt

Setup Instructions

1. Clone repository
   git clone
   cd trading_bot

2. Install dependencies
   pip install -r requirements.txt

3. Create .env file
   BINANCE_API_KEY=your_testnet_api_key
   BINANCE_API_SECRET=your_testnet_api_secret

4. Setup Binance Testnet
   Use Binance Futures Testnet
   Generate API keys from
   https://testnet.binancefuture.com/

Usage

1. Manual mode
   python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

2. Limit order
   python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 80000

3. Auto mode (dataset-based)
   python cli.py --symbol BTCUSDT --type MARKET --quantity 0.001 --auto

Example Output

1. Fear and Greed Index: 45
2. Current Price: 74800
3. SMA(10): 74200
4. Signal from dataset: BUY

ORDER SUMMARY

1. Symbol: BTCUSDT
2. Side: BUY
3. Type: MARKET
4. Quantity: 0.001

RESPONSE

1. Order ID: 12345678
2. Status: NEW
3. Executed Qty: 0.001
4. Avg Price: 74850

Logging

1. All logs are saved in trading_bot.log

Assumptions

1. Datasets contain required columns
2. value for Fear and Greed Index
3. close for historical data
4. Latest row is the most recent data
5. Testnet is used

Requirements

1. python-binance
2. python-dotenv
3. pandas

Deliverables Covered

1. Market and Limit orders
2. Buy and Sell support
3. CLI input handling
4. Structured code
5. Logging
6. Exception handling
7. Dataset integration

Bonus Features

1. Data-driven trading
2. Two dataset integration
3. SMA calculation
4. Auto trading mode

Future Improvements

1. Add RSI or EMA
2. Add Stop-Limit orders
3. Improve CLI
4. Add UI

Author

Mehar Chhina
