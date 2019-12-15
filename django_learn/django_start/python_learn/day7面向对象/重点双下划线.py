class School(object):
    def __init__(self,name,addr,type):
        self.name = name
        self.addr = addr
        self.type = type
    def __repr__(self):
        return "School(%s,%s)"%(self.name,self.addr)
    def __str__(self):
        return "Scholl(%s,%s)"%(self.name,self.type)

    # def __del__(self):
    #     print('程序被是否啦')
# 格式化方式
#释放程序
s =School('new','beijing','mid')


print(repr(s))
print(s)
#str函数或者print函数调用时，---》obj.__str__()
# repr函数交互式解释器中调用时---》obj.___repr__
# 如果__str__没有被定义，那么就会使用__repr__来代替输出
# 注意，这两方法返回值必须是字符串，否则抛出异常