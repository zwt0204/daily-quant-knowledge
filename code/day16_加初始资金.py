initial_cash = 100000
strategy_returns = [0.01, -0.02, 0.015, 0.005]

cash = initial_cash
for r in strategy_returns:
    cash = cash * (1 + r)
    print("当前资金:", round(cash, 2))

print("最终资金:", round(cash, 2))
