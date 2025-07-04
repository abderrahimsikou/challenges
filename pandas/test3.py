import pandas as pd

data = {
    'Reg': ['x', 'y', 'z'],
    'Selles': [500, 1500, 200]
}

df = pd.DataFrame(data)
print(df)

total = df.groupby('Reg')['Selles'].sum()
print(total)