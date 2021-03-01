# 乗算レイヤー

class MulLayer:
    def __init__(self):#initialize(初期化)
        self.x = None
        self.y = None
    
    def forward(self, x, y):#順伝播
        self.x = x
        self.y = y
        out = x * y

        return out
    
    def backward(self, dout):#逆伝播
        dx = dout * self.y # xとyをひっくり返す
        dy = dout * self.x

        return dx, dy


apple = 100
apple_num = 2
tax = 1.1

#layer
mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

#forward　順伝播
apple_price = mul_apple_layer.forward(apple, apple_num)
price = mul_tax_layer.forward(apple_price, tax)

#print(price)
## --> 220.00000000000003

#backward　逆伝播
dprice = 1
dapple_price, dtax = mul_tax_layer.backward(dprice)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)

#print(dapple, dapple_num, dtax)
## --> 2.2 110.00000000000001 200





