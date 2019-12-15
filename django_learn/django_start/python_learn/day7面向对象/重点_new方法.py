# __new__在__init__之前执行

class Student(object):
    def __init__(self,name):
        self.name = name
        print('hh')

    def __new__(cls, *args, **kwargs):
        #负责执行__init__，进行一些实例初始化前的工作
        print(cls,args,kwargs)
        return object.__new__(cls)

p =Student('lsj')
p.name


#设计模式：23 gof 单例设计模式

# class Print(object):
#     tasks = []
#     instance = None
#     def __init__(self,name):
#         self.name = name
#     def add_task(self,job):
#         self.tasks.append(job)
#         print('%s 添加%s任务到打印机,总任务数%s'%(self.name,job,len(self.tasks)))
#     def __new__(cls, *args, **kwargs):
#         #只有第一次实例化的时候，正常进行，后面每次进行实例化，并不能创建一个新的实例
#         if cls.instance is None:
#             #进行正常的实例化，并把实例化的对象传到instance里面
#             obj = object.__new__(cls) ##把每次实例化的对象存下来，
#             cls.instance = obj
#         return cls.instance  #把第一次实例化的对象返回给实例化的实例，实例化胡，再进行__init__
#
# p1 = Print('word app')
# p2 = Print('pdf app')
# p3 = Print('excel app')
#
# p1.add_task('work file')
# p2.add_task('pdf file')
# p3.add_task('excel file')
#
# #第二次，第三次实例化的时候，实际是对第一次实例化的值进行修改，并不是真正的实例化了
# print(p1.name,p2.name,p3.name)