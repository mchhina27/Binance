import pandas as pd


# -----------------------------
# PREPROCESS FEAR & GREED
# -----------------------------
def preprocess_fear_greed(csv_path: str):
    df = pd.read_csv(csv_path)

    # Normalize column names
    df.columns = df.columns.str.lower().str.strip()

    # Auto-detect value column
    if "value" not in df.columns:
        for col in df.columns:
            if "value" in col or "fear" in col:
                df.rename(columns={col: "value"}, inplace=True)

    # Convert to numeric
    df["value"] = pd.to_numeric(df["value"], errors="coerce")

    # Clean data
    df = df.dropna(subset=["value"])
    df = df.drop_duplicates()
    df = df.reset_index(drop=True)

    return df


# -----------------------------
# PREPROCESS HISTORICAL DATA
# -----------------------------
def preprocess_historical(csv_path: str):
    df = pd.read_csv(csv_path)

    # Normalize column names
    df.columns = df.columns.str.lower().str.strip()

    # Try to find price column
    possible_cols = ["close", "closing_price", "price", "last", "adj close"]

    found = None
    for col in df.columns:
        if col in possible_cols or "close" in col or "price" in col:
            found = col
            break

    if not found:
        raise ValueError(f"No price column found in dataset. Columns: {df.columns.tolist()}")

    # Rename to standard
    df.rename(columns={found: "close"}, inplace=True)

    # Convert to numeric
    df["close"] = pd.to_numeric(df["close"], errors="coerce")

    # Clean
    df = df.dropna(subset=["close"])
    df = df.drop_duplicates()

    # Sort if date exists
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df = df.sort_values(by="date")

    df = df.reset_index(drop=True)

    return df

# -----------------------------
# SIGNAL GENERATION
# -----------------------------
def get_signal(fear_greed_path: str, historical_path: str):
    fg_df = preprocess_fear_greed(fear_greed_path)
    hist_df = preprocess_historical(historical_path)

    # Latest values
    fg_value = float(fg_df.iloc[-1]["value"])

    # Calculate SMA
    hist_df["sma_10"] = hist_df["close"].rolling(window=10).mean()

    latest = hist_df.iloc[-1]
    price = float(latest["close"])
    sma = float(latest["sma_10"])

    print(f"Fear & Greed Index: {fg_value}")
    print(f"Current Price: {price}")
    print(f"SMA(10): {sma}")

    # Decision logic
    if fg_value < 40 and price > sma:
        return "BUY"
    elif fg_value > 60 and price < sma:
        return "SELL"
    else:
        return "BUY"  # fallback


# -----------------------------
# PLOT STRATEGY
# -----------------------------
def plot_strategy(fear_greed_path: str, historical_path: str):
    import matplotlib.pyplot as plt

    fg = preprocess_fear_greed(fear_greed_path)
    hist = preprocess_historical(historical_path)

    # Align lengths
    min_len = min(len(fg), len(hist))
    fg = fg.tail(min_len).reset_index(drop=True)
    hist = hist.tail(min_len).reset_index(drop=True)

    # Calculate SMA
    hist["sma"] = hist["close"].rolling(window=10).mean()

    buy_x, buy_y = [], []
    sell_x, sell_y = [], []

    for i in range(min_len - 1):
        value = fg.loc[i, "value"]
        price = hist.loc[i, "close"]

        if value < 50:
            buy_x.append(i)
            buy_y.append(price)
        else:
            sell_x.append(i)
            sell_y.append(price)

    # Plot
    plt.figure()

    plt.plot(hist["close"], label="Price")
    plt.plot(hist["sma"], label="SMA(10)")

    if buy_x:
        plt.scatter(buy_x, buy_y, label="BUY")

    if sell_x:
        plt.scatter(sell_x, sell_y, label="SELL")

    plt.legend()
    plt.title("Trading Strategy Visualization")

    plt.savefig("strategy_plot.png")
    plt.show()