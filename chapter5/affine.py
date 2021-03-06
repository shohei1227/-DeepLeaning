import numpy as np

class Affine:
    def __init__(self, w, b):
        self.w = w
        self.b = b
        self.x = None
        self.dw = None
        self.dy = None
    
    def forward(self, x):
        self.x = x
        out = np.dot(x, self.w) + self.b

        return out
    
    def backward(self, dout):
        dx = np.dot(dout,self.w.t)
        self.dw = np.dot(self.x.t, dout)
        self.db = np.sum(dout, axis=0)

        return dx


