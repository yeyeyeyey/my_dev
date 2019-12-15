# 变量可以指向函数，函数的参数能接受变量，那么一个函数就可以接收另一个函数作为参数

def add(x,y,f):
    return f(x)+f(y)

re = add(3,4,abs)
print(re)