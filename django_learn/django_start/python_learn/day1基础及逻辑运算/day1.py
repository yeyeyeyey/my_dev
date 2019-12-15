# import getpass
# name = input("请输入你的姓名")
#
# pwd = getpass.getpass("请输入你的密码：")
# print("hello "+ name)
#
# print(pwd)

# import sys
# print(sys.argv) #把执行脚本时传递的参数获取到了
#
#
########
# import os,sys
# # os.system("df -h")调用系统命令
# # print(sys.argv)
# os.system(''.join(sys.argv[1:]))
# """
# python tab补全模块
# """
# import sys
# import readline
# import rlcompleter
#
# if sys.platform == 'darwin' and sys.version_info[0] ==2:
#     readline.parse_and_bind("bind^I rl_complete")
# else:
#     readline.parse_and_bind("tab:complete")
# for i in range(10):
#     if i <5:
#         continue
#     if i >7:
#         break
#     print(i)

# count =0
# while count in range(0,100):
#     print("你是风儿，我是杀")
#     count +=1
#     if count ==10:
#         print("挺远")
#         break

#三级菜单

# menu = {
#     '早餐':{
#         '主食':{'粉':{'螺蛳粉','桂林米粉'},'面':{'兰州拉面','牛肉面'},'粥':{'皮蛋瘦肉粥','白粥'}},
#         "零食":'士力架,泡面,''火腿肠'
#     },
#     '中餐':{
#         '川菜':['鱼香肉丝','酸辣肉丁','麻辣鸡丝'],
#         '湘菜':['辣椒炒肉','红烧肉','水煮鱼片'],
#         '粤菜':['烧鹅饭','白贝汤','耗油菜心']
#     },
#     # '中餐':'{"川菜":"鱼香肉丝"},{"湘菜":"辣椒炒肉"},{"粤菜":"烧鹅饭"}',
#     '晚餐':[{"面食":"包子"},{"水果":"香蕉"},{"饮料":"可乐"}]
# }
# print("这有三种选择，你想选哪个")
# for items in menu.items():
#     print(items[0])
#
# eat = input("早餐，中餐，晚餐，你想吃什么呢~\n")
#
# if eat == "早餐":
#     for k,v in menu[eat].items():
#         print(k)
#         type = input("主食,零食，你想吃什么呢~\n")
#         if type =='主食':
#             for k,v in menu[eat]['主食'].items():
#                 print(k)
#                 # print(menu[eat]['主食'])
#             food = input("你想吃什么呢~\n")
#             if food == '粉':
#                 print(menu[eat]['主食']['粉'])
#             # else:
#             #     break
#         elif type =='零食':
#             print(menu[eat]['零食'])
#         break
# elif eat =='中餐':
#     for k, v in menu[eat].items():
#         print(k)
#     # # #     for items in m
#     # # # for items in
#     # print(menu['早餐'])
#     # for k,v in menu['早餐'].items():
#     #     print(k)

####三元表达式####
# a = input("请输入a的值")
# b = input("请输入b的值")
# re =  int(a)+int(b) if a>b else int(a)-int(b)
# print(re)


####lambda表达式###
#
# a =lambda x,y:x+y
# print(a(5,7))
#
##一切皆对象，对象基于类创建

