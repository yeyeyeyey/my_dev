#把一个方法变成一个静态的属性（即静态变量）

class Dog(object):
    # money = 1000
    def __init__(self,name):
        self.name = name

    @property
    def setname(self):
        money = 1000
        print("这狗要 %s 元"%money)
    @setname.setter
    def setname(self,money):
        self.money = money
        print("这狗要 %s 元"%money)
    @setname.deleter
    def setname(self):
        print("清掉了狗的价格")

d = Dog('ss')
d.setname

d.setname = 2000
del d.setname