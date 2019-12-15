a = {'a':'123','b':'234','c':'456'}
# print(a['a'])
# a['a'] = 999
# print(a)
#删除
# a.pop('c')
# del a['a']
#随机删除
# print(a.popitem())

# print(a)
#
#查找
# get()或者a['a']
#get()找不到的话，不会报错
# print(a.get('c'))

#直接打印k或v值
# print(type(a.keys()),a.values())
#setdefault新增一组数据
# print(a)
# a.setdefault('u','dsd')
# # print(a)
    # b= {1:2,3:4,'dsd':'ddd'}
    # #update新增一组数列
    # a.update(b)
    # print(a)
#items
# print(a.items())
#列表生成式，生成默认dict
b = dict.fromkeys([1,2,3],'dds')
print(b)