import pandas as pd

df = pd.DataFrame({
    'strategy_ret': [0.00, 0.02, -0.01, 0.03, -0.02]
})

df['equity'] = (1 + df['strategy_ret']).cumprod()
print(df)
