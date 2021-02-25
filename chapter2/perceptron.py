#パーセプトロンの実装

"""
def AND(x1, x2):
    w1, w2 , theta = 0.5, 0.5, 0.7#これらはANDゲートを表現する重みの一例に過ぎない
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

print(AND(0, 0))
print(AND(1, 0))
print(AND(0, 1))
print(AND(1, 1))

print("#################################")
"""

#thetaを閾値としていたが、-thetaをたしあわせて、0よりも大きいか小さいかを判断するようにする。
#ここでのthetaはバイアス(thetaではなく、bと表記される)と呼ばれる。
import numpy as np
x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7
print("w * x = ", w * x)
print(np.sum(w * x))
print(np.sum(w * x) + b)


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

print("AND(0, 0) = ", AND(0, 0))
print("AND(1, 0) = ", AND(1, 0))
print("AND(0, 1) = ", AND(0, 1))
print("AND(1, 1) = ", AND(1, 1))
print("##################################")

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

print("NAND(0, 0) = ", NAND(0, 0))
print("NAND(1, 0) = ", NAND(1, 0))
print("NAND(0, 1) = ", NAND(0, 1))
print("NAND(1, 1) = ", NAND(1, 1))
print("####################################")


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

print("OR(0, 0) = ", OR(0, 0))
print("OR(1, 0) = ", OR(1, 0))
print("OR(0, 1) = ", OR(0, 1))
print("OR(1, 1) = ", OR(1, 1))