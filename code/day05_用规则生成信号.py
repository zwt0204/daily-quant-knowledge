import pandas as pd

df = pd.DataFrame({
    'close': [10.0, 10.3, 10.1, 10.5, 10.8]
})

df['ma2'] = df['close'].rolling(2).mean()
df['ma3'] = df['close'].rolling(3).mean()
df['signal'] = (df['ma2'] > df['ma3']).astype(int)
print(df)
