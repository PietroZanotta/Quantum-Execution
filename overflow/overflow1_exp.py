# visualize performance of overflow1

from overflow1 import simulate_classical_circ
import pandas as pd
import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np

keys_to_sum = ['1000']

df = pd.DataFrame(columns=['iteration', 'sum'])

for n_iter in range(1, 11):
    data = simulate_classical_circ(1000, n_iter, False)
    total_sum = sum(data.get(key, 0) for key in keys_to_sum)
    df = df.append({'iteration': n_iter, 'sum': total_sum}, ignore_index=True)


plt.scatter(df['iteration'], df['sum'], color='blue')
x = df['iteration'].values
y = df['sum'].values

linear_interpolation = interpolate.interp1d(x, y, kind='linear')

x_new = np.linspace(x.min(), x.max(), 500)
y_new = linear_interpolation(x_new)

plt.scatter(x, y, color='blue', label='Original Data')
plt.plot(x_new, y_new, color='red', label='Linear Interpolation')

plt.xlabel('FPQS iteration')
plt.ylabel('Precision')

plt.show()

