import pandas as pd
import matplotlib.pyplot as plt

price = pd.Series([10, 10.2, 10.1, 10.4, 10.6, 10.8, 10.7, 11.0, 11.2, 11.1,
                   11.4, 11.6, 11.5, 11.7, 11.9, 11.6, 11.3, 11.1, 10.9, 10.8])
df = pd.DataFrame({"close": price})
df["ma5"] = df["close"].rolling(5).mean()
df["ma20"] = df["close"].rolling(20).mean()

df["signal"] = (df["ma5"] > df["ma20"]).astype(int)
df["position"] = df["signal"].shift(1).fillna(0)
df["ret"] = df["close"].pct_change().fillna(0)
df["strategy_ret"] = df["position"] * df["ret"]
df["equity"] = (1 + df["strategy_ret"]).cumprod()

buy = (df["signal"] == 1) & (df["signal"].shift(1).fillna(0) == 0)
sell = (df["signal"] == 0) & (df["signal"].shift(1).fillna(0) == 1)

fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
axes[0].plot(df.index, df["close"], label="Close", linewidth=2)
axes[0].plot(df.index, df["ma5"], label="MA5", linestyle="--")
axes[0].plot(df.index, df["ma20"], label="MA20", linestyle=":")
axes[0].scatter(df.index[buy], df.loc[buy, "close"], marker="^", s=80, label="Buy")
axes[0].scatter(df.index[sell], df.loc[sell, "close"], marker="v", s=80, label="Sell")
axes[0].set_title("Price / Moving Averages / Buy-Sell")
axes[0].legend()

axes[1].plot(df.index, df["equity"], color="purple", linewidth=2)
axes[1].set_title("Strategy Equity Curve")
plt.tight_layout()
plt.show()
