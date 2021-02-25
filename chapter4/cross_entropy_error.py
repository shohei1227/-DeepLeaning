import numpy as np

def cross_entropy_error(y, t):
    delta = 1e-7#微小な値を生成し、0の時にマイナス無限大にならないようにする。
    return -np.sum(t * np.log(y + delta))