profits = [100, -50, 80, -30, 120]

total_profit = sum(profits)
win_count = len([x for x in profits if x > 0])
win_rate = win_count / len(profits)

print("累计收益:", total_profit)
print("胜率:", win_rate)
