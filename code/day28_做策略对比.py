strategies = {
    "双均线": "趋势市",
    "ETF轮动": "强弱分化的趋势环境",
    "网格": "震荡市"
}

market = "震荡市"

print(f"当前市场环境: {market}\n")

for name, suitable_market in strategies.items():
    if suitable_market == market:
        print(f"{name} 更匹配当前环境")
    else:
        print(f"{name} 不是当前环境的优先选择")
