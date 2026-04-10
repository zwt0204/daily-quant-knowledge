import pandas as pd

df = pd.DataFrame({
    'close': [10.0, 10.3, 10.1, 10.5]
})

df['ret'] = df['close'].pct_change()
print(df)
