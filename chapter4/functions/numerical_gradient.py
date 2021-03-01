import numpy as np

def function_2(x):
    return x[0] ** 2 + x[1] ** 2



#まとめて偏微分を計算し、全ての変数の偏微分をベクトルとしてまとめる（勾配）

def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x) #xと同じ形状の配列を生成

    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = tmp_val + h #x+hにして、再び同じ配列の同じ場所に格納
        fxh1 = f(x) #f(x + h)

        x[idx] = tmp_val - h #x-hにして、再び同じ配列の同じ場所に格納
        fxh2 = f(x) #f(x - h)
        grad[idx] = (fxh1 -fxh2) / (2 * h)
        x[idx] = tmp_val
    return grad        
"""
print(numerical_gradient(function_2, np.array([3.0, 4.0])))
print(numerical_gradient(function_2, np.array([0.0, 2.0])))
print(numerical_gradient(function_2, np.array([3.0, 0.0])))
print(numerical_gradient(function_2, np.array([-3.0, 0.0])))
#print(numerical_gradient(function_2, np.array([[-0.20838863, -0.34024908,  -1.29517191], [-0.45216316, 0.39368814, 0.52020035]])))
k = np.array([[-0.20838863, -0.34024908,  -1.29517191], [-0.45216316, 0.39368814, 0.52020035]])
print(k.size)
"""

def numerical_gradient_multi(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x)
    
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        x[idx] = tmp_val + h
        fxh1 = f(x) # f(x+h)
        
        x[idx] = tmp_val - h 
        fxh2 = f(x) # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2*h)
        
        x[idx] = tmp_val # 値を元に戻す
        it.iternext()   
        
    return grad