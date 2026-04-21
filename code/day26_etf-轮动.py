# 一个最简单的 ETF 轮动示例

etf_returns = {
    "沪深300ETF": 0.021,
    "中证500ETF": 0.054,
    "红利ETF": 0.032,
}

best_etf = max(etf_returns, key=etf_returns.get)
best_return = etf_returns[best_etf]

print("本期应选择的ETF:", best_etf)
print("近20天收益率:", f"{best_return:.2%}")
