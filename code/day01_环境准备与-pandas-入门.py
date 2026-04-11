price_today = 105
ma5 = 103
ma20 = 100
holding = False

if ma5 > ma20 and not holding:
    print("买入信号")
elif ma5 < ma20 and holding:
    print("卖出信号")
else:
    print("继续观察")
