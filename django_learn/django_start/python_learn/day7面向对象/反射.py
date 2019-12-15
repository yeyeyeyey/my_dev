#反射，可以通过字符串的形式来操作对象的属性

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def walk(self):
        print("跑路咯")

def talk(self):
    print('%s在讲话'%self.name)
p = Person('lsj','25')
print(p)
# hasattr()
# if hasattr(p,'name'):
#     print("有这个属性")
#增删改查


# getattr()

# fuc = input("大佬你试试").strip()
# if hasattr(p,fuc):
#     fuc = getattr(p,fuc)
#     fuc()



# setattr()
# setattr(p,'sex','male')
# setattr(p,'speak',talk)#对实例增加一个静态方法
# p.speak(p)
#
# setattr(Person,'speak2',talk) #推荐使用，对类增加一个静态方法
# p.speak2()
# print(p.sex)
# p.talk()
# delattr()


# delattr(p,'age')
# del p.age
# p.age






# 如何反射一个文件下的 指定的字符串对应的属性

#__name__在当前模块主动执行的情况下(不是被导入执行）,等于__main__
# 在被其他模块导入使用时，等于模块名称
#
# print(__name__)  #__main__代表模块本身
#
# if __name__ =='__main__': #只会在被别的模块导入时发生作用
#     print('hh')
#

#反射查找文件
# import sys
#
# mod = sys.modules[__name__]
# if hasattr(mod,'p'):
#     o = getattr(mod,'p')
#     print(o)