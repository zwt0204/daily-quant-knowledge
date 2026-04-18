import pandas as pd

close = pd.Series([100, 101, 103, 102, 104, 106, 105, 107, 109, 108, 110, 111])
params = [(3, 5), (3, 8), (5, 8)]

split = int(len(close) * 0.7)
in_sample = close.iloc[:split]
out_sample = close.iloc[split:]

def backtest(series, short_win, long_win):
    short_ma = series.rolling(short_win).mean()
    long_ma = series.rolling(long_win).mean()
    signal = (short_ma > long_ma).astype(int)
    ret = series.pct_change().fillna(0)
    strategy_ret = signal.shift(1).fillna(0) * ret
    return (1 + strategy_ret).prod() - 1

best_param = None
best_score = -999

for short_win, long_win in params:
    score = backtest(in_sample, short_win, long_win)
    print(f"in-sample: {(short_win, long_win)} -> {score:.2%}")
    if score > best_score:
        best_score = score
        best_param = (short_win, long_win)

out_score = backtest(out_sample, best_param[0], best_param[1])
print(f"best param = {best_param}")
print(f"out-of-sample: {out_score:.2%}")
