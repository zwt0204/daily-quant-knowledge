import pandas as pd

df = pd.DataFrame({"close": [10, 10.2, 10.5, 10.1, 10.8]})

print(df["close"])
print(df[df["close"] > 10.2])
df["prev_close"] = df["close"].shift(1)
df["ma3"] = df["close"].rolling(3).mean()
print(df)
