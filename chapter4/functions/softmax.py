import numpy as np

"""
a = np.array([0.3, 2.9, 4.0])
exp_a = np.exp(a)
print(exp_a)
# --> [1.34985881 18.17414537 54.59815003]

sum_exp_a = np.sum(exp_a)
print(sum_exp_a)
# --> 4.1221542101633

y = exp_a/sum_exp_a

print(y)
# --> [0.01821127 0.24519181 0.73659691]
"""
"""
def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

#この関数で実際のソフトマックス関数の式を表すことができているが、e**10やe**100となる値が非常に大きくなり、オーバーフローが起こりうる


a = np.array([1010, 1000, 990])
print(softmax(a))
# --> [nan nan nan]と出力される。これはオーバーフローしてしまっており、正しく計算されていないことを示している。

c = np.max(a)
print(a - c)
print(np.exp(a - c) / np.sum(np.exp(a - c)))
"""
def softmax_revised(a):
    c = np.max(a)
    exp_a_r = np.exp(a - c)#オーバーフロー対策
    sum_exp_a_r = np.sum(exp_a_r)
    y = exp_a_r / sum_exp_a_r
    return y
    

