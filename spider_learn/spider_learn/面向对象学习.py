class Dog(object):
    def __init__(self,name,age,attact,master):
        self.name = name
        self.age = age
        self.attact = attact
        self.master = master
        self.sayhi()
    def sayhi(self):
        print("hi,I am %s ,I am %s ,my master is %s"%(self.name,self.age,
                                                      self.master.name))
class Person(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def walk_dog(self,cat):
        print("%s 带着 %s 去散步"%(self.name,cat.name))

p1 = Person('lisi',25,'M')
dog1 = Dog('jinmao',3,15,p1)
p1.walk_dog(dog1)