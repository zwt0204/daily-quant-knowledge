import pandas as pd

df = pd.DataFrame({
    'close': [10.0, 10.3, 10.1, 10.5],
    'position': [0, 0, 1, 1]
})

df['ret'] = df['close'].pct_change().fillna(0)
df['strategy_ret'] = df['position'].shift(1).fillna(0) * df['ret']
print(df)
