prices = [100, 102, 101, 99, 97, 94, 96]
entry_price = prices[0]
stop_loss = entry_price * 0.95
holding = True

for i, price in enumerate(prices):
    if holding and price < stop_loss:
        print(f"day {i}: stop loss triggered at {price}")
        holding = False
        break

if holding:
    print("no stop loss triggered")
