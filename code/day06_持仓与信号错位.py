def average(a, b):
    return (a + b) / 2

prices = [10, 10.2, 10.5]

for p in prices:
    if p > 10:
        print("价格大于 10:", p)

print("平均值:", average(10, 12))
