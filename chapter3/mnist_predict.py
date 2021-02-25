import sys, os
sys.path.append(os.pardir)
#print(os.getcwd())# --> Users/shoheinoguchi/DeepLeaning/DeepLeaning-first
import numpy as np
from dataset.mnist import load_mnist
from activation_function.sigmoid_func import sigmoid
from activation_function.softmax import softmax_revised
import pickle

def get_data():
    (_, _), (x_test, t_test) = \
        load_mnist(normalize=True, flatten=True, one_hot_label=False)#正規化あり
    return x_test, t_test


def init_network():
    """
    picleファイルのsample_weight.pklに保存された学習済みの重みパラメータを読み込む
    重みとバイアスのパラメータがディクショナリ型で保存されている
    """
    with open("chapter3/dataset/sample_weight.pkl", 'rb') as f:
        #sys.path.append(os.pardir)で親ディレクトリのファイルをインポートするために設定する。
        #その後にsample_weight.pklのある　pathを通す
        network = pickle.load(f)
    
    return network


def predict(network, X):
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]

    a1 = np.dot(X, W1) + b1
    z1 = sigmoid(a1)

    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)

    a3 = np.dot(z2, W3) + b3
    y = softmax_revised(a3)

    return y


x, t = get_data()
network = init_network()

accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p = np.argmax(y)#もっとも確率の高い要素のインデックスを取得
    if p == t[i]:
        accuracy_cnt += 1

print("Accuracy ;", float(accuracy_cnt) / len(x))
# --> 0.9352


