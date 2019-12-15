# 一个socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来确定一个socket
# 1.初始化socket
# 2.bind端口
# 3.accept监听
# 4.read（）
# 5.write
# 6.read
# 7.close
import socket
import threading
#实例化一个socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定端口，监听短裤
s.bind(('127.0.0.1',9999))

#传入的参数指定等待连接的最大数量
s.listen(5)
print("waiting for connection...")
# res = s.accept()
# print(res)
# while True:
#     #接受一个新连接：
#     sock,addr = s.accept()
#     t = threading.Thread(target=tcplink,args=(sock,addr))
#等待连接
conn,addr = s.accept()

#收发消息  1024为接受数据的最大数值，单位：bytes
data = conn.recv(1024)
print("客户端的数据是",data)

#服务端再发消息
conn.send(data.upper())

#连接中断
conn.close()

#网络中断
s.close()