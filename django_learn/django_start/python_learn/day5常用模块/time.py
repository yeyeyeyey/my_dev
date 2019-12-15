#时间模块
# import time
# import datetime
# # print(time.time())
# # print(time.altzone)
# # print(time.asctime()) #返回本地时间
# # print(time.asctime(time.localtime()))
# # print(time.gmtime(time.time()))
# # print(time.ctime())
# print(datetime.datetime.now()) #时间戳直接转化成日期格式
# print(datetime.datetime.now()+datetime.timedelta(3))#当前时间+3天
# print(datetime.datetime.now()+datetime.timedelta(hours=-3))#当前时间+3天

#random模块

import random
# print(random.randint(0,1999))#打印0-1999之间的数
# print(random.randint(1,2))
# print(random.randrange(1,293434))

#生成随机验证码
# checkcode= ''
# for i in range(4):
#     current = random.randrange(0,4)
#     if current !=1:
#         temp = chr(random.randint(65,90))
#     else:
#         temp = random.randint(0,9)
#     checkcode +=str(temp)
# print(checkcode)
# code = ''
# for i in range(0,4):
#     a = chr(random.randint(65,90))
#     code += str(a)
# print(code)


import os

# print(os.path)


import sys
# print(sys.argv)
#
# print(sys.version_info)
#
# print(sys.path)
# print(sys.platform)

import shutil  #文件处理

import json

