# class User(object):
#     def login(self):
#         print("login")
#
#     def save(self):
#         print('save')
#
#     def register(self):
#         print('register')
#
# u =User()
#
# while 1:
#     a = input('请输入').strip()
#     if hasattr(u,a):
#         b = getattr(u,a)
#         b()
data = {'a':'123'}
old_data = {'c':'1234'}
def repalce():
    b = input('输入一个值')
    if data.get(b) == None:
        print(old_data['c'])
    else:
        print(data[b])
repalce()
# print()