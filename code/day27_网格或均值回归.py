prices = [100, 102, 101, 99, 98, 95]
window = 5
current_price = prices[-1]
mean_price = sum(prices[-window:]) / window

threshold = 0.03  # 偏离 3%

print(f"当前价格: {current_price}")
print(f"5日均价: {mean_price:.2f}")

if current_price < mean_price * (1 - threshold):
    print("价格低于均值较多 -> 可能出现均值回归买点")
else:
    print("价格没有明显偏离均值 -> 暂时不触发信号")
