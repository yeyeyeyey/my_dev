# import os
# print (os.path)
# f= open('testfile','a')
#f.readline
# #'r'只读模式/默认模式
# #'w'写入模式，没有文件则新建
# #'a'追加模式，
# r =f.write('这是新增数据')
#"b"表示处理二进制文件（如：FTP发送上传ISO镜像文件，linux可忽略，windows处理二进制文件时需标注）
#
# rb
# wb
# # ab
# with open('newfile','a') as b:
#     b.write('这是新数据')

# with语句，为了避免打开文件后忘记关闭，可以管理上下文

f1 = open('testfile','r')
f2 = open('addanewfile','a')
# f1.readline()
# f2 = f1.readlines()
for line in f1.readlines():
    line = line.replace('o','%')
    print(line)
    f2.write(line)
# f2.close()
