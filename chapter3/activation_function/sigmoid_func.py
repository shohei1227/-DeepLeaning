import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

"""
x = np.array([-1.0, 1.0, 2.0])
print(sigmoid(x))


t = np.array([1.0, 2.0, 3.0])
print(1.0 + t)

print(1.0 / t)

x = np.arange(-10.0, 10.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)#y軸の範囲を指定
plt.show()
"""