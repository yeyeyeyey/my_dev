# os.getpid os.getppid 获取子线程，获取父线程
# import os
# print("processing (%s) start ..."%os.getpid())
# pid = os.fork()
# if pid ==0:
#     print('I am a child process %s and my parent is %s'%(os.getpid(),
#                                                          os.getppid()))
# else:
#     print('I %s just created a child process %s '%(os.getpid(),pid))
#brew install yarn

from multiprocessing import Process
# import os
#
# def run_proc(name):
#     print('Run child process %s (%s)...'%(name,os.getpid()))
#
# import threading
# import time
# def sayhi(num):
#     print('running on number:%s '%num)
#     time.sleep(3)
#
# if __name__ == '__main__':
#     ti = threading.Thread(target=sayhi,args=(1,))
__author__ = 'lsj'

import time
import threading

def run(n):
    print('[%s]------running'%n)
    time.sleep(2)
    print('done')

def main():
    for i in range(5):
        t = threading.Thread(target=run,args=['子进程%s'%i,])
        t.start()
        t.join(1)
        print('start threading',t.getName())

m = threading.Thread(target=main,args=[])
m.setDaemon(False) #将main线程设置为Daemon线程，它作为程序主线程的守护线程  True时为守护线程，结束时，整个线程都会结束
m.start()
m.join(timeout=1)
print('----mainjob-----')