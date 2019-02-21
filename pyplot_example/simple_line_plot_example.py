import numpy as np
import matplotlib
import matplotlib.pyplot as plt

t = np.arange(0.0, 2.0, 0.1)
print(t)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t,s)

ax.set(xlabel='time (s)',
       ylabel='voltage (mV)',
       title='A simple plot')

ax.grid()

fig.savefig("test.png")
       
plt.show()
