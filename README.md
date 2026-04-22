Binance Futures Trading Bot (CLI-Based)

This is a command-line trading bot that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M). It also supports data-driven trading using Fear and Greed Index and historical price data.

Features

Place MARKET and LIMIT orders
Supports BUY and SELL
Works with Binance Futures Testnet
Takes input from CLI using argparse
Uses dataset-based trading logic
Performs data preprocessing
Uses Simple Moving Average (SMA)
Logs API requests and responses
Handles errors and exceptions

Strategy Logic

The bot uses two datasets.

Fear and Greed Index is used to understand market sentiment.

Historical price data is used to calculate SMA (10-period).

Decision logic:
BUY when sentiment is low and price is above SMA
SELL when sentiment is high and price is below SMA
Fallback ensures a trade is always executed

Project Structure

trading_bot/
bot/
client.py
orders.py
validators.py
strategy.py
cli.py
fear_greed_index.csv
historical_data.csv
trading_bot.log
requirements.txt
README.md

Setup Instructions

1. Clone repository
   git clone <your-repo-link>
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

Manual mode
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 80000

Auto mode (dataset-based)
python cli.py --symbol BTCUSDT --type MARKET --quantity 0.001 --auto

Example Output

Fear and Greed Index: 45
Current Price: 74800
SMA(10): 74200

Signal from dataset: BUY

ORDER SUMMARY
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

RESPONSE
Order ID: 12345678
Status: NEW
Executed Qty: 0.001
Avg Price: 74850

Logging

All logs are saved in trading_bot.log

Assumptions

Datasets contain required columns
value for Fear and Greed Index
close for historical data
Latest row is the most recent data
Testnet is used

Requirements

python-binance
python-dotenv
pandas

Deliverables Covered

Market and Limit orders
Buy and Sell support
CLI input handling
Structured code
Logging
Exception handling
Dataset integration

Bonus Features

Data-driven trading
Two dataset integration
SMA calculation
Auto trading mode

Future Improvements

Add RSI or EMA
Add Stop-Limit orders
Improve CLI
Add UI

Author

Mehar Chhina
