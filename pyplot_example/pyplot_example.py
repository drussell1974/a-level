import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

print(x1)
print(y1)

plt.subplot(2,1,1)
plt.plot(x1, y1, 'o-')
plt.title('2 subplots')
plt.ylabel('damped oscillation')

plt.show()
