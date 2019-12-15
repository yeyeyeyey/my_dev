# a =iter([3,1,2,33])
# # print(a.__next__(),a.__next__(),a.__next__())
# # for i in a:
# #     print(i)
#
# b = (x**2 for x in range(5))#这是一个生成器，需要用next()方法一个个去拿数
# # 把（）变成[]就变成了列表表达式
# # 把列表表达式的【】变成（）就变成了生成器，创建一个列表时，列表容量是有限的，所以我们在循环使用的时候一遍循环
# # 一边计算去生成，就叫生成器，generator。
# #生成器保留的是算法，每次调用的时候就去计算，如果没有更多元素，就报错，也是可迭代对象
# # print(b.__next__())
# a = [1,2,4,5,6,756,54]
# c = [i+1 for i in a]
# # print(c)
# print(next(b))

#赋值语句 a,b=b,a+b
def fib(i):
    if i == 1:
        return 1
    if i ==2:
        return 1
    if i>2:
        return fib(i-1)+fib(i-2)
def func(n):
    for i in range(1,n+1):
        yield (fib(i))
b = func(6)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))

#把函数变成生成器的方法，即把return变成yield
