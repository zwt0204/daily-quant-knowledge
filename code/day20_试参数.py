import pandas as pd
import akshare as ak

# 取日线数据（示例：平安银行）
df = ak.stock_zh_a_hist(symbol="000001", period="daily", adjust="qfq")
df = df[["日期", "收盘"]].copy()
df["日期"] = pd.to_datetime(df["日期"])
df = df.sort_values("日期").set_index("日期")

def test_ma_strategy(data, short_win, long_win):
    d = data.copy()
    d["ma_short"] = d["收盘"].rolling(short_win).mean()
    d["ma_long"] = d["收盘"].rolling(long_win).mean()
    d["signal"] = (d["ma_short"] > d["ma_long"]).astype(int)
    d["ret"] = d["收盘"].pct_change()
    d["strategy_ret"] = d["signal"].shift(1) * d["ret"]
    total_return = (1 + d["strategy_ret"].fillna(0)).cumprod().iloc[-1] - 1
    trade_count = d["signal"].diff().abs().fillna(0).sum() / 2
    return round(total_return, 4), int(trade_count)

for short_win, long_win in [(5, 20), (10, 30), (20, 60)]:
    total_return, trade_count = test_ma_strategy(df, short_win, long_win)
    print(f"MA{short_win}/{long_win}: 收益={total_return}, 交易次数={trade_count}")
