import pandas as pd

price = pd.DataFrame({'close': [10, 10.2, 10.5, 10.1, 10.8, 11.0, 10.7]})

for short_win, long_win in [(2, 3), (3, 5)]:
    df = price.copy()
    df[f'ma{short_win}'] = df['close'].rolling(short_win).mean()
    df[f'ma{long_win}'] = df['close'].rolling(long_win).mean()
    df['signal'] = (df[f'ma{short_win}'] > df[f'ma{long_win}']).astype(int)
    print(f'params=({short_win}, {long_win})')
    print(df[['close', 'signal']])
