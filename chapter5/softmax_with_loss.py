import os, sys 
sys.path.append(os.pardir)

import numpy as np
from chapter4.functions import softmax, cross_entropy_error

class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None #損失
        self.y = None #ソフトマックス関数の出力
        self.t = None #教師データ

    def forward(self, x, t):
        self.t = t
        self.y =softmax.softmax_revised(x)
        self.loss = cross_entropy_error,cross_entropy_error(self.y, self.t)

        return self.loss
    
    def backward(self, dout=1):
        batch_size =self.t.shape[0]
        dx = (self.y - self.t) / batch_size

        return dx


