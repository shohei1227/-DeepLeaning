#多次元配列
import numpy as np

A = np.array([1.0, 2.0, 3.0, 4.0])
print("A = \n", A)
print("次元数 = ", np.ndim(A))
print("shape = ", A.shape)

B = np.array([[1, 2], [3, 4], [5, 6]])
print("B = \n", B)
print("次元数 = ", np.ndim(B))
print("shape = ", B.shape)

print("##########################################")
#行列の掛け算
a = ([[1, 2], [3, 4]])
b = ([[5, 6], [7, 8]])

print("a * b = \n", np.dot(a, b))#np.dot()はdot積を意味する。１次元ではベクトル、２次元では行列の積を計算する
#np.dot(a, b)とnp.dot(b, a)では異なる値になる
print("b * a = \n", np.dot(b, a))

#3*2行列と2*3行列の掛け算も同じようにnp.dot()で計算できる
#行列は左の列数と右の行数が等しくなければならない
