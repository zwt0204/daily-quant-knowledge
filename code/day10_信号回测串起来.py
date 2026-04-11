import pandas as pd

df = pd.DataFrame({"close": [10, 10.1, 10.3, 10.2, 10.5, 10.8, 10.7]})
df["ma3"] = df["close"].rolling(3).mean()
df["ma5"] = df["close"].rolling(5).mean()
print(df)
