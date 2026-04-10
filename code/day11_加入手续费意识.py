import pandas as pd

df = pd.DataFrame({
    'position': [0, 1, 1, 0, 1],
    'ret': [0.00, 0.01, 0.02, -0.01, 0.03]
})

fee = 0.001
trade = df['position'].diff().abs().fillna(0)
df['strategy_ret'] = df['position'].shift(1).fillna(0) * df['ret'] - trade * fee
print(df)
