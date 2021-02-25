#1.5.2 ~  Numpyの基本

import numpy as np

print("############################")
print("Numpy配列の生成")
x = np.array([1.0, 2.0, 3.0])
print("x = ", x)

print("type(x) = ", type(x))

print("############################")

print("Numpyの算術計算")
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print("x = ", x, ", y = ",y)

sum = x + y
sub = x - y
print("sum = ", sum)
print("sub = ", sub)

mul = x * y
div = x / y
print("mul = ",mul)
print("div = ",div)


div2 = x / 2.0
print("div2 = ", div2)


print("###############################")

print("NumpyのN次元配列")

A = np.array([[1, 2], [3, 4]])
print("A = ", A)


print("A.shape = ", A.shape)
print("A.dtype = ", A.dtype)

B = np.array([[3, 0], [0, 6]])
print("A + B = \n", A + B)
print("A * B = \n", A * B)


print("###############################")
print("broadcast(ブロードキャスト)")

C = np.array([[10, 20]])
print("A = \n", A)
print("C = ", C)
print("A * C = \n", A * C)
print("C * A = \n", C * A)

print("###############################")
print("要素へのアクセス")

print("A = \n", A)

print("A[0] = ", A[0])
print("A[1] = ", A[1])
print("A[0][1] = ", A[0][1])

print("A.flatten = ", A.flatten())#一次元に変換
print("A > 3 = \n", A > 3)