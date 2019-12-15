# 递归特性:
#
# 1. 必须有一个明确的结束条件
#
# 2. 每次进入更深一层递归时，问题规模相比上次递归都应有所减少
#
# 3. 递归效率不高，递归层次过多会导致栈溢出（在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢

def cal(n):
    print(n)
    if int(n/2) ==0:
        return n
    return cal(int(n/2))

def jiecheng(n):
    if n == 1:
        return n
    return n*jiecheng(n-1)
print(jiecheng(5))