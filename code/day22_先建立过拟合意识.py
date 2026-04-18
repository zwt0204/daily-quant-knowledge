import pandas as pd

# 示例价格
close = pd.Series([100, 101, 103, 102, 104, 107, 106, 108, 110, 109, 111, 113])

params = [(3, 5), (3, 8), (5, 8)]

for short_win, long_win in params:
    short_ma = close.rolling(short_win).mean()
    long_ma = close.rolling(long_win).mean()

    signal = (short_ma > long_ma).astype(int)
    ret = close.pct_change().fillna(0)
    strategy_ret = signal.shift(1).fillna(0) * ret
    cum_return = (1 + strategy_ret).prod() - 1

    print(f"short={short_win}, long={long_win}, cumulative_return={cum_return:.2%}")
