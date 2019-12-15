# import asyncio
# @asyncio.coroutine
# def hello():
#     print('hello world')
#     r = yield from asyncio.sleep(1)
#     print('hello again')
# #获取eventloop
# loop = asyncio.get_event_loop()
# #执行coroutine
# loop.run_until_complete(hello())
# loop.close()

import threading,asyncio

async def hello():
    print('hello world (%s)'%threading.currentThread())
    await asyncio.sleep(1)
    print('hello again!(%s)'%threading.currentThread())
loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
#
# import asyncio
# @asyncio.coroutine
# def wget(host):
#     print('wget %s ...'%host)
#     connect = asyncio.open_connection(host,80)
#     reader,writer = yield from connect
#     header = 'GET /HTTP/1.0\r\nHOST: %s\r\n\r\n' %host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header >%s'%(host,line.decode('utf-8').rstrip()))
#     writer.close()
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in['www.sina.com','www.sohu.com','www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()