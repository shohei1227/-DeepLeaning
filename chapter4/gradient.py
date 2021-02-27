import os
import numpy as np
from functions import softmax
from functions import cross_entropy_error
from functions.numerical_gradient import numerical_gradient_multi
class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3) #ガウス分布で初期化
        #randomで重みを設定している
    
    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax.softmax_revised(z)
        loss = cross_entropy_error.cross_entropy_error(y, t)
        return loss

net = simpleNet()
print("ランダムで初期化された重み = \n", net.W)
print("###############################")
x = np.array([0.6, 0.9])
p = net.predict(x)

print("predict = ",p)
print("###############################")

print("最大値のインデックス = ", np.argmax(p))

t = np.array([0, 0, 1]) #正解ラベル
print(net.loss(x, t))


f = lambda w: net.loss(x, t)#引数wはダミー
dW = numerical_gradient_multi(f, net.W)

print(dW)