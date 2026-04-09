import pandas as pd

df = pd.DataFrame({'close': [10, 10.2, 10.5, 10.1, 10.8, 11.0, 10.7]})
df['ma2'] = df['close'].rolling(2).mean()
df['ma3'] = df['close'].rolling(3).mean()
df['signal'] = (df['ma2'] > df['ma3']).astype(int)
df['ret'] = df['close'].pct_change().fillna(0)
df['strategy_ret'] = df['signal'].shift(1).fillna(0) * df['ret']
df['equity'] = (1 + df['strategy_ret']).cumprod()
print(df)
