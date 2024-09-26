# visualize performance of fpqs when M = 1 and N = 64

from fpqs import simultare_fpqs_circ
import pandas as pd
import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np

keys_to_sum = ['111111']

df = pd.DataFrame(columns=['iteration', 'sum'])

for n_iter in range(1, 11):
    data = simultare_fpqs_circ(100, False, n_iter, 6, False)

    reversed_dict = {}

    # Iterate through the dictionary
    for key, value in data.items():
        # Extract the first 4 digits and reverse them
        reversed_key = key[::-1][:6]
        # Store the reversed key and the original value in the new dictionary
        reversed_dict[reversed_key] = value

    total_sum = sum(reversed_dict.get(key, 0) for key in keys_to_sum)
    df = df.append({'iteration': n_iter, 'sum': total_sum}, ignore_index=True)


plt.scatter(df['iteration'], df['sum'], color='blue')
x = df['iteration'].values
y = df['sum'].values

linear_interpolation = interpolate.interp1d(x, y, kind='linear')

x_new = np.linspace(x.min(), x.max(), 100)
y_new = linear_interpolation(x_new)

plt.scatter(x, y, color='blue', label='Original Data')
plt.plot(x_new, y_new, color='red', label='Linear Interpolation')

plt.xlabel('FPQS iteration')
plt.ylabel('Precision')

plt.show()

simultare_fpqs_circ(100, num_qubit=6, plot=False)