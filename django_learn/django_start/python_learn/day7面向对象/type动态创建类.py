# call方法，对面后面加括号，触发执行
class Student(object):
    def __init__(self,name):
        self.name = name
        print('hh')

s = Student('lsj')
print(type(s))


print(type(Student))


def __init__(self,name,age):
    self.name = name
    self.age = age
#一切皆对象，type为元素
dog = type('Dog',(object,),{'role':'dog','__init__':__init__})
# print(type(dog))
d = dog('lsj',22)
print(d.age)
