import socket

sock = socket.socket()

sock.bind(('127.0.0.1',8801))

sock.listen(5)##最大链接数目

while 1:
    print("server waiting......")
    conn,ddr=sock.accept()
    data = conn.recv(1024)
    print('data',data)
    conn.send(b"HTTP/1.1 200 ok\r\n\r\nhello luffycity!")
    conn.close()