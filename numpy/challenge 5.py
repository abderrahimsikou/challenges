import numpy as np

array = np.array([10, 9, 12, 29, 45, 28, 35])

seuil = 15

x = np.where(array > seuil)[0]
new = array[x]
print(new)