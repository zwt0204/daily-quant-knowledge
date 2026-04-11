cash = 100000
position_ratio = 0.5
max_loss_ratio = 0.05

position_money = cash * position_ratio
max_loss_money = position_money * max_loss_ratio

print("本次投入资金:", position_money)
print("这一笔最多愿意亏:", max_loss_money)
