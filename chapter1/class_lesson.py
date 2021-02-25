#1.4.2 クラス

class Man:
    def __init__(self, name):#constructor(コンストラクタ)-->クラスのインスタンスが作成されるとき一度だけ呼ばれる
        #print("self = ", self) #<__main__.Man object at 0x7f9160246cd0>
        #print("name = ", name) #Shohei
        self.name = name#nameという引数を取り、その引数でインスタンス変数であるself.nameを初期化する。
        print("Initialized")
    
    def hello(self):
        print("Hello", self.name, "!")

    def goodbye(self):
        print("Good-bye", self.name, "!")
    
    
m = Man("Shohei")#Manというクラスからmというインスタンス(オブジェクト)を生成する。
m.hello()
m.goodbye()
print(type(Man))