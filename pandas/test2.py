import pandas as pd

data = {
    'ID': [1,2,3,4],
    'Price': [500, 1500, 200, 1200],
    'Catego': ['Food', 'Electro', 'Agrico','Close']
}

df = pd.DataFrame(data)

x = df[df['Price'] > 1000]
print(x)