# 内层函数调用外层函数。
# 返回的函数对象，不仅仅是一个函数对象，在该函数外还包裹了一层作用域，这使得，该函数无论在何处调用，优先使用自己外层包裹的作用域


#开闭原则：
# 1.对已实现的功能模块不应该修改
# 2.对现有的功能的扩展开发
def outer():
    name = '好好听课'
    def inner():
        print("你要干嘛",name)
    return inner

fun = outer()
# fun()


def plus(n):
    return n+1
plus2 = lambda x:x+1
a = plus
print(a(2))

#闭包+高阶函数，变成装饰器
