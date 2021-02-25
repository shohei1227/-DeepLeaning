import step_func as step#chapter3/step_func/をimport
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5.0, 5.0, 0.1)#xの範囲を定める --> -5.0から5.0まで0.1単位で
y = step.step_func(x)#chapter3/step_func/のstep_func関数を使う
plt.plot(x, y)#plot
plt.ylim(-0.1, 1.1)#yの範囲を定める
plt.show()

