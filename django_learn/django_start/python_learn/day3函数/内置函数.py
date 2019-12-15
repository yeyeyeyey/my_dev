# #集合
# 1. 集合
# 主要作用:
#
# 去重
# 关系测试， 交集＼差集＼并集＼反向(对称)差集
# 2. 元组　　
# 只读列表，只有count, index 2 个方法
#
# 作用：如果一些数据不想被人修改， 可以存成元组，比如身份证列表

# 3.字典
#
# key-value对
# 特性：
# 无顺序
# 去重
# 查询速度快，比列表快多了
# 比list占用内存多
# 为什么会查询速度会快呢？因为他是hash类型的，那什么是hash呢？
#
# 哈希算法将任意长度的二进制值映射为较短的固定长度的二进制值，这个小的二进制值称为哈希值。哈希值是一段数据唯一且极其紧凑的数值表示形式。如果散列一段明文而且哪怕只更改该段落的一个字母，随后的哈希都将产生不同的值。要找到散列为同一个值的两个不同的输入，在计算上是不可能的，所以数据的哈希值可以检验数据的完整性。一般用于快速查找和加密算法
#
# dict会把所有的key变成hash 表，然后将这个表进行排序，这样，你通过data[key]去查data字典中一个key的时候，python会先把这个key hash成一个数字，然后拿这个数字到hash表中看没有这个数字， 如果有，拿到这个key在hash表中的索引，拿到这个索引去与此key对应的value的内存地址那取值就可以了。
#
# 在说明这两个原因之前，先说个概论，字典的快是建立在用空间换时间，切记！还记得之前说的，数组缺点是在创建时规定了大小，当其空白占位达到其大小的1/3时，Python会重新引入一个更大的空间，此时会将原有空间的元素一一拷贝，再将新增的元素一一拷贝进去，所以这会造成巨大的空间浪费，同时在产生新空间的同时，会同步规划元素的hash值(hash值会变得更大)，此时由于hash值的不同，则可能导致键的次序不同。另一个原因则是散列冲突，当添加新建的时候发现散列冲突，则新键可能会被安排到另一个位置，于是添加的元素可能就会跑到前方去了。以上就是关于无序的字典解释。
# ————————————————
# 版权声明：本文为CSDN博主「sandwu」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_42681866/article/details/82785127


#函数 带有默认参数时，不填写则显示默认参数，填写则展示填写的参数，关键参数必须放在位置参数后面
#默认参数
def func(name,age,country = 'CN'):
    print("name",name)
    print("age",age)
    print("country",country)

# func('lsj',25,'english')
#关键参数

def a(name,age,*args):
    print(name,age,args)

# a('aa',23,232,4535,64)
# 返回aa 23 (232, 4535, 64)，*args返回的数据为一个列表

def b(name,age,*args,**kwargs):
    print(name,age,args,kwargs)
# b(1,2)
#1 2 () {} ,*8kwargs返回的数据为一个字典

name = 'lsj'
def change_name(name):
    print("before name",name)
    name = '炫酷boy'
    print("after name",name)
# change_name(name='s')
# print(name)

#return 代表函数的结束，如果未知名return，则函数返回值为None


# compile() 函数将一个字符串编译为字节代码。
a= open('递归.py')
d = compile(a.read(),'','exec')
# exec (d)

msg = "又回到最初的原点"
f = open('addanewfile','w')
print(msg,'你是个sb',  sep="|",end="",file=f)
#切片，等同于3：8：2
a= range(20)
pattern = slice(3,8,2)
for i in a[pattern]:
    print(i)