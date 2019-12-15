#类方法 类方法只能访问类变量，不能访问实例变量
class Dog(object):
    name = 'dog'
    def __init__(self,name):
        self.name = name

    @classmethod
    def eat(self):
        print('%s在吃哦'%self.name)


d = Dog('jinmao')
d.eat()
print(d.eat)