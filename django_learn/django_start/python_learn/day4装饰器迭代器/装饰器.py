account = {
    'user_status':False,
    'username':'lsj',
    'pwd':'123'
}

def login(auth):
    def auth(func):
        def inner(*args,**kwargs):
            if account['user_status'] is False:
                username = input("请输入你的用户名\n")
                pwd = input("请输入你的密码\n")
                if username == account['username'] and pwd== account['pwd']:
                    print("登录成功")
                    account['user_status'] = True
                    # func(*args, **kwargs)
                else:
                    print("还咩登录啊")
            else:
                print("用户已登录，验证通过")
                # func(*args,**kwargs)
            if account['user_status'] is True:
                return func(*args,**kwargs)
        return inner
    return auth
def home():
    print("首页")

@login('weixin')
def american():
    print("欧美专区")

@login('qq')
def henan(*args,**kwargs):
    print("河南专区")


henan()
american()

# # 装饰器，把函数作为一个参数传给另一个函数




# user_status = False #用户登录了就把这个改成True
#
# def login(auth_type): #把要执行的模块从这里传进来
#     def auth(func):
#         def inner(*args,**kwargs):#再定义一层函数
#             if auth_type == "qq":
#                 _username = "alex" #假装这是DB里存的用户信息
#                 _password = "abc!23" #假装这是DB里存的用户信息
#                 global user_status
#
#                 if user_status == False:
#                     username = input("user:")
#                     password = input("pasword:")
#
#                     if username == _username and password == _password:
#                         print("welcome login....")
#                         user_status = True
#                     else:
#                         print("wrong username or password!")
#
#                 if user_status == True:
#                     return func(*args,**kwargs) # 看这里看这里，只要验证通过了，就调用相应功能
#             else:
#                 print("only support qq ")
#         return inner #用户调用login时，只会返回inner的内存地址，下次再调用时加上()才会执行inner函数
#
#     return auth
#
# def home():
#     print("---首页----")
#
# @login('qq')
# def america():
#     #login() #执行前加上验证
#     print("----欧美专区----")
#
# def japan():
#     print("----日韩专区----")
#
# @login('qq')
# def henan(style):
#     '''
#     :param style: 喜欢看什么类型的，就传进来
#     :return:
#     '''
#     #login() #执行前加上验证
#     print("----河南专区----")
#
# home()
# # america = login(america) #你在这里相当于把america这个函数替换了
# #henan = login(henan)
#
# # #那用户调用时依然写
# america()
# henan('33')
