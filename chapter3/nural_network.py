# nural_network(隱れ層２つ)

import numpy as np
from activation_function import sigmoid_func
from activation_function import identify_func

#入力層から第１層
X = np.array([1.0, 0.5])#入力値が1.0と0.5
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])#重みの行列
B1 = np.array([0.1, 0.2, 0.3])#バイアス
#上の三つは適当に割り振った


print("X.shape = ", X.shape)
print("W1.shape = ", W1.shape)
print("B1.shape = ", B1.shape)

A1 = np.dot(X, W1) + B1
print("A1 = ", A1)

Z1 = sigmoid_func.sigmoid(A1)

print("Z1 = ", Z1)

#第１層から第２層
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])
#上の２つは適当に割り振った

print("Z1.shape = ", Z1.shape)
print("W2.shape = ", W2.shape)
print("B2.shape = ", B2.shape)

A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid_func.sigmoid(A2)
print("A2 = ", A2)
print("Z2 = ", Z2)

#第２層から出力層
W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])
#上の２つは適当に割り振った

A3 = np.dot(Z2, W3) + B3
Y = identify_func.identify_func(A3)

print("Y = ", Y)

