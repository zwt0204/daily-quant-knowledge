cash = 10000
max_position_ratio = 0.5
planned_orders = [2000, 5000, 8000, 12000]

max_position = cash * max_position_ratio

for order in planned_orders:
    actual_order = min(order, max_position)
    print(f"planned: {order}, actual: {actual_order}")
