# 迭代器，可以用next()方法进行调用并返回下一个值的，都是迭代器，iterator
# 比如某个函数是可迭代的，循环函数等等就是迭代器

# from collections import Iterator
#
# print(isinstance((x for x in range(10)),Iterator))

# 字符串、字典、列表是可迭代对象，但不是迭代器

# 凡是可作用于for循环的对象都是Iterable类型；
#
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
#
# Python的for循环本质上就是通过不断调用next()函数实现的，例如：
#
# 1
# 2
# for x in [1, 2, 3, 4, 5]:
#     pass

