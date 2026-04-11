buy_price = 10.0
sell_price = 10.3
shares = 100
fee = 5
slippage = 3

gross_profit = (sell_price - buy_price) * shares
net_profit = gross_profit - fee - slippage

print("毛收益:", gross_profit)
print("净收益:", net_profit)
