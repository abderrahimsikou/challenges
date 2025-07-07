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
#print(df)
df['nom'].str.upper()
#print(df)
df = df.rename(columns={'ville':'localisation'})
#print(df)
