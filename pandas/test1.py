import pandas as pd
import numpy as np

data = {
    'A': [4, 5, np.nan, 7],
    'B': [4, np.nan, 9, 7],
    'C': [4, 6, 9, np.nan]
}

print(data)
df = pd.DataFrame(data)
print(df)

fill = df.fillna(df.mean())
print(fill)