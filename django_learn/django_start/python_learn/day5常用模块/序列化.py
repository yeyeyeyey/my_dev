#json数据与字典数据的转化
import json
dic = {'a':123,'b':234,'c':456}
st = 'gdgdfggdf'
# d= json.dumps(dic)
# print(d,type(d))
#
# a = json.loads(d)
# print(a,type(a))

#把字典数据序列化为json文件
# with open('xx.json','w') as j:
#     json.dump(dic,j)


#pickle，序列化
import pickle

# p_str = pickle.dumps(dic)
# print(p_str)

# d_ = pickle.loads(p_str)
# print(d_)
d = {'k':123,'l':242}
dw ='sdfsdf'
# with open('xx','wb') as p:
#     pickle.dump(d,p)

#持久化
# shelve模块是一个简单的k,v将内存数据通过文件持久化的模块，可以持久化任何pickle可支持的python数据格式
import shelve

d = shelve.open('testfile')
class Test(object):
    def __init__(self,n):
        self.n = n

t = Test(334234)
t2 = Test(324535)

name = ['lsj','sfsf','fsff']
d['test'] = name
d['t1'] = t
d['t2'] = t2

d.close()