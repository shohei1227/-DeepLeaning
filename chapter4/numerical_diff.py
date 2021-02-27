import numpy as np

def numerical_diff(f, x):
    h = 1e-4 #0.0001
    return (f(x+h) - f(x-h)) / (2*h) #誤差が生じるため、中心差分をとる
    
def pri_f(f):
    return f * 5