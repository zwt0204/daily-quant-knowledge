import pandas as pd

df = pd.DataFrame({"close": [10, 10.1, 10.3, 10.2, 10.5, 10.8, 10.7]})
df["ret"] = df["close"].pct_change().fillna(0)
df["buy_hold"] = (1 + df["ret"]).cumprod()

df["ma3"] = df["close"].rolling(3).mean()
df["ma5"] = df["close"].rolling(5).mean()
df["signal"] = (df["ma3"] > df["ma5"]).astype(int)
df["position"] = df["signal"].shift(1).fillna(0)
df["strategy_ret"] = df["position"] * df["ret"]
df["strategy_equity"] = (1 + df["strategy_ret"]).cumprod()

print(df[["buy_hold", "strategy_equity"]])
