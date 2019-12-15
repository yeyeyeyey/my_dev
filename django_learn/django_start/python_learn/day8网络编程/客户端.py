import socket
#
# # 1.初始化socket
# # 2.band端口
# # 3.accept监听
# # 4.read（）
# # 5.write
# # 6.read
# # 7.close
# # 创建一个socket：
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #建立连接：
# s.connect(('www.sina.com',80))
#
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#
# #接受数据
# buffer = []
# while True:
#     #每次最多接受1k字符
#     d = s.recv(1024)
#     if d :
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
#
# #接受数据时，一次最多接受指导字节数，无限while循环，直到返回空数据，表示接受完毕，退出循环
# s.close()
#
# header ,html = data.split(b'\r\n\r\n',1)
# print((header.decode('utf-8')))
# with open('sina.html','wb') as f:
#     f.write(html)
#初始化套接字
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#连接
s.connect(('127.0.0.1',9999))

#发收消息
s.send('hello'.encode('utf-8'))
data = s.recv(1024)
print(data)

#关闭连接
s.close()

