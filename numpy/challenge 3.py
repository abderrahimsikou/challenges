import numpy as np

data1 = np.array([4, 6, 9, 2])
data2 = np.array([4, 3, 9, 7])

different = np.where(data1 != data2)[0]
print(data1[different])
print(data2[different])

