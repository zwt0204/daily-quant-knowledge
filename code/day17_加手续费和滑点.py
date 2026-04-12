import pandas as pd

# 示例价格与信号（1 表示持有，0 表示空仓）
df = pd.DataFrame({
    'close': [100, 102, 101, 104, 103],
    'signal': [0, 1, 1, 0, 1]
})

# 价格收益率
df['ret'] = df['close'].pct_change().fillna(0)

# 持仓收益：用前一天信号，避免未来函数
df['strategy_ret_raw'] = df['signal'].shift(1).fillna(0) * df['ret']

# 是否发生交易（开仓/平仓/换仓都算）
df['trade'] = df['signal'].diff().abs().fillna(0)

fee = 0.001      # 手续费
slippage = 0.0005  # 滑点
cost = (fee + slippage) * df['trade']

# 扣成本后的策略收益
df['strategy_ret_net'] = df['strategy_ret_raw'] - cost

# 资金曲线
initial_cash = 100000
df['equity_raw'] = initial_cash * (1 + df['strategy_ret_raw']).cumprod()
df['equity_net'] = initial_cash * (1 + df['strategy_ret_net']).cumprod()

print(df[['close', 'signal', 'trade', 'strategy_ret_raw', 'strategy_ret_net', 'equity_raw', 'equity_net']])
