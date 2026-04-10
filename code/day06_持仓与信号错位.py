import pandas as pd

df = pd.DataFrame({
    'signal': [0, 1, 1, 0, 1]
})

df['position'] = df['signal'].shift(1).fillna(0)
print(df)
