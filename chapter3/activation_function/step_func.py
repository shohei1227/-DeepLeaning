"""def step_func(x):
    if x > 0:
        return 1
    else:
        return 0
"""
#上の状態だとxの引数は実数しか入力することができず、Numpy配列を引数にとるような使い方はできない。
#そのため、修正する
import numpy as np
def step_func(x):
    y = x > 0#numpy配列に対して不等号の演算を行い、bool型(True/False)で返す
    return y.astype(np.int)#astype()はnumpy配列の型の変換を行う-->この場合はbool型をint型にする。つまりTrue＝1, False＝0になる。
