class Relu:
    def __init__(self):
        self.mask = None
        #インスタンス変数maskはTrue/FalseからなるNumpy配列
    
    def forward(self, x):
        self.mask = (x <= 0)#x <= 0 でTrue、それ以外でFalse に設定
        out = x.copy()
        out[self.mask] = 0

        return out
    
    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout

        return dx