import pandas as pd

df = pd.DataFrame({
    "date": ["2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31"],
    "close": [10.0, 10.2, 10.1, 10.4]
})

print(df.head())
