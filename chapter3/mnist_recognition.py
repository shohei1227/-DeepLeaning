#import sys, os
#sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image


#print(help(load_mnist))

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)
    #normalizeで正規化(0.0 ~ 1.0)
    #flattenで１次元配列にするかどうか
    #one_hot_labelでone-hot表現にするかどうか(正解を１、それ以外を０とするか)

img = x_train[0]
label = t_train[0]
print("label = ", label)#5


"""
print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)
"""

print("img.shape = ", img.shape)
img = img.reshape(28, 28)#形状を元の画像サイズに変形
print("img.shape（reshaped） = ", img.shape)
#flatten=Trueとして読み込んだのでnumpy配列として１次元で格納されているため、画像の表示の際には28*28のサイズにreshapeする必要がある。

img_show(img)
