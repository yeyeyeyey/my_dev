# class Studens(object):
#     _instance = None
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             obj = object.__new__(cls)
#             cls._instance = obj
#         return cls._instance
#     def pri(self):
#         print("test")
# a = Studens('lsj',25)
# b = Studens('sd',12)
# print(a)
# a.pri()
# print(id(a))
# print(id(b))

class Msg(object):
    instance = None
    def __init__(self,qudao,info):
        self.qudao = qudao
        self.info = info

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            obj = object.__new__(cls)
            cls.instance =obj
        return cls.instance
    def pri(self):
        print("test")
a = Msg('a','a')
b = Msg('a','a')
a.pri()
b.pri()
print(id(a),id(b))