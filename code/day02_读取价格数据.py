import pandas as pd
from io import StringIO

csv_text = """date,close
2026-03-24,10.0
2026-03-25,10.3
2026-03-26,10.1
"""

df = pd.read_csv(StringIO(csv_text))
print(df.head())
