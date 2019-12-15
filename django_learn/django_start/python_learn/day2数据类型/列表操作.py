# import copy
# #列表
# name = ['lsj','sss','ddf','woie','sdsfe','sss']
# b= [1,3,5]
# a ={'d':'123','a':'345','e':'2323','f':{'g':'dsf'}}
# #切片
# # print(name[0:2])
# # print(name[1:-1])
# # print(name[-1:])
# #追加
# # name.append('新增的')
# #插入,数字表示插在第几个数字后面
# # name.insert(1,'新插入的数据')
# # name.insert(-1,'新插入的数据')
# #修改
# # name[1] = '修改后的'
# #删除
# # del name[1]
# #删除指定元素
# # name.remove('lsj')
# #删除最后一个值
# # name.pop()
# #倒叙排列
# # name.reverse()
# #扩展
# # name.extend(b)
# #拷贝，无法拷贝嵌套内的函数
# # name2 = name.copy()
# #深拷贝
#     # 对于字典 元组 和列表来说，进行浅拷贝和深拷贝时，内存的地址是不同的
#     #发现内存中地址的值都是完全相同
#     # 浅拷贝只会拷贝内存中的第一层数据
#
# # 而对于深拷贝来说将会把所有数据重新创建
# # b = copy.deepcopy(a)
# # # print(id(a))
# # # print(id(b))
# # # print((a))
# # # print(b)
# # # print(id(b))
# # # print(id(a))
# # a['f']['g']='eee'
# # # b['f']= '2'
# # print(b)
# # print(a)
# """
# 拷贝字符串和数字时，因为他们的内存都指向同一个地址，所以深拷贝和浅拷贝是一致的
#
# 对于列表，元祖，字典
# 浅拷贝，只拷贝第一层
# 深拷贝，可以拷贝全部数据
# """
# #统计
# # print(name.count('sss'))
# #排序
# # name.sort()
# # print(name)
# #反转
# # name.reverse()
# #获取下标，只返回第一个下标
#
# print(name.index('ddf'))

# 元组
# 元组其实跟列表差不多，也是存一组数，只不是它一旦创建，便不能再修改，所以又叫只读列表

#购物车程序
money = input("你有夺少钱呐~\n")
print("商品列表如下：")
a = [['111','表',100],['222','衣服',200],['333','书',30]]
for i in range(len(a)):

    print(a[i][0],a[i][1])
goods = input("你想买个啥呢\n")
if goods =='表':
    left =int(money)- a[0][2]
elif goods =='衣服':
    left =int(money)- a[1][2]
elif goods =='书':
    left = int(money) - a[2][2]
else:
    print("老铁你到底要啥呀")
if left > 0:
    print("买完了%s，您还剩%s" %(goods,left))
else:
    print("您的钱不够呢")

    # 2.
    # 元组　　
    # 只读列表，只有count, index
    # 2
    # 个方法
    #
    # 作用：如果一些数据不想被人修改， 可以存成元组，比如身份证列表