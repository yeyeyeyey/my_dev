

#静态方法，不能访问类变量，也不能访问实例变量
# @staticmethod 把一个方法变成静态方法
# 普通方法，需要实例化后直接调用，并且可以self.调用实例变量或类变量
#静态方法隔断了
class Dog(object):
    def __init__(self,name):
        self.name = name

    @staticmethod
    def eat(self):
        print('%s在吃哦'%self.name)
    @staticmethod
    def fly():
        print('flying')
a = Dog('jinmao')
a.fly()
a.eat(a)
# a.eat(a)可以选择在