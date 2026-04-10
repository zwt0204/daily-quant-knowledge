import pandas as pd

df = pd.DataFrame({
    'equity': [1.00, 1.05, 1.03, 1.08, 1.02]
})

df['peak'] = df['equity'].cummax()
df['drawdown'] = df['equity'] / df['peak'] - 1
print(df)
