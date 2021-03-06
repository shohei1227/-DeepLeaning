import numpy as np
from functions import cross_entropy_error
from functions import softmax
from functions import sigmoid_func
from functions import numerical_gradient


class TwoLayerNet:

    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)

    def predict(self, x):
        W1, W2 = self.params['W1'], self.params['W2']
        b1, b2 = self.params['b1'], self.params['b2']

        a1 = np.dot(x, W1) + b1
        z1 = sigmoid_func.sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        y = softmax.softmax_revised(a2)

        return y
    
    #x:入力データ、t:教師データ
    def loss(self, x, t):
        y = self.predict(x)
        
        return cross_entropy_error.cross_entropy_error(y, t)
    
    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        t = np.argmax(t, axis=1)

        accuracy = np.sum(y == t) / float(x.shape[0])

        return accuracy
    
    def numerical_gradient(self, x, t):
        loss_W = lambda W: self.loss(x, t)
        grads = {}

        grads['W1'] = numerical_gradient.numerical_gradient_multi(loss_W, self.params['W1'])
        grads['b1'] = numerical_gradient.numerical_gradient_multi(loss_W, self.params['b1'])
        grads['W2'] = numerical_gradient.numerical_gradient_multi(loss_W, self.params['W2'])
        grads['b2'] = numerical_gradient.numerical_gradient_multi(loss_W, self.params['b2'])

        return grads


net = TwoLayerNet(input_size=784, hidden_size=100, output_size=10)
print(net.params['W1'].shape)
print(net.params['b1'].shape)
print(net.params['W2'].shape)
print(net.params['b2'].shape)

print("#####################################")

from dataset import mnist

(x_train, t_train), (x_test, t_test) = mnist.load_mnist(normalize=True, one_hot_label=True)

#ハイパーパラメータ
iters_num = 10000
#print(x_train.shape) #(60000, 784)
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.1

train_loss_list = []

network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

for i in range(iters_num):
    #ミニバッチの取得
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    #勾配の計算
    grad = network.numerical_gradient(x_batch, t_batch)

    #パラメータの更新
    for key in ("W1", "b1", "W2", "b2"):
        network.params[key] = learning_rate * grad[key]
    
    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)
    print(train_loss_list)



