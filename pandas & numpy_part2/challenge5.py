import pandas as pd
import numpy as np

data=[
       ["Amine", 28, "Casablanca"],
       ["Lina", 22, "Rabat"],
       ["Youssef", 35, "Fès"],
       ["Salma", 30, "Casablanca"],
       ["Nora", np.nan, "Tanger"]]

df = pd.DataFrame(data, columns=['nom','age','ville'])

df['Année de Naissance'] = 2025 - df['age']

df = df.sort_values(by='age', ascending=False)

new_data = df.drop(columns='Année de Naissance')
print(new_data)

new_data = df.drop(index=0)
print(new_data)