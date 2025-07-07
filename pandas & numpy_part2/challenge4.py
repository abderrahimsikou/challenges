import pandas as pd
import numpy as np

data=[
       ["Amine", 28, "Casablanca"],
       ["Lina", 22, "Rabat"],
       ["Youssef", 35, "Fès"],
       ["Salma", 30, "Casablanca"],
       ["Nora", np.nan, "Tanger"]]

df = pd.DataFrame(data, columns=['nom','age','ville'])

print(df.isnull().sum)
mean      = df['age'].mean
df['age'] = df['age'].fillna(mean)
