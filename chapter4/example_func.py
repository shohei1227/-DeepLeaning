import sys, os

import numpy as np
import matplotlib.pyplot as plt
import numerical_diff

def function_1(x):
    return 0.01 * x ** 2 + 0.1 * x


#微分すると0.02x + 0.1


print(numerical_diff.numerical_diff(function_1, 5)) #-->実際は0.2
print(numerical_diff.numerical_diff(function_1, 10)) #-->実際は0.3
"""
出力値は
0.1999999999990898
0.2999999999986347
"""

x = np.arange(0.0, 100.0, 0.1) #0から20まで0.1刻みのx配列
y = function_1(x)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
plt.show()

