#加算レイヤー
class AddLayer:
    def __init__(self):
        pass#何も行わなくていいため初期化はpassする

    def forward(self, x, y):
        out = x + y 
        return out
    
    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1

        return dx, dy

