#__doc__ 表示类的描述信息
class Foo(object):
    def fun(self):
        pass
print(Foo.__doc__)
f = Foo()
#表示当前操作的对象在哪个模块

print(f.__module__)
#表示当前操作的对象的类是什么

print(f.__class__)


# typeh创建动态类


