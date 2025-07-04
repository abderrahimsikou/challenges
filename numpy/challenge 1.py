import numpy as np

temperature = np.array([15, 19, 23, 28, 30, 40])

moyene   = np.mean(temperature)
meadiane = np.median(temperature)
std      = np.std(temperature)

print('moyene:', moyene)
print('mediane:', meadiane)
print('std:', std)


