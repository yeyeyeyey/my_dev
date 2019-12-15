# call方法，对面后面加括号，触发执行
class Student(object):
    def __init__(self,name):
        self.name = name
        print('hh')
    def __call__(self, *args, **kwargs):
        print(self,args,kwargs)

s = Student('lsj')
s()