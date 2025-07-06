import pandas as pd

data = {
    'produit': ['x','x', 'y', 'y','z','z'],
    'vente': [100,210 ,150,180 ,240,310],
    'region': ['nord', 'sud','nord', 'sud', 'nord', 'nord']
}

df = pd.DataFrame(data)
print(df)

pivot = pd.pivot_table(df, values='vente', index='produit', columns='region', aggfunc=sum)
print(pivot)