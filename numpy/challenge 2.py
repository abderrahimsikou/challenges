import numpy as np

tableau = np.array([10, 22, 15, 23])

moyene = np.mean(tableau)
std    = np.std(tableau)

normaliser = (tableau - moyene) / std

print(normaliser)
