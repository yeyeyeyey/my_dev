# Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
#
# 我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：


from multiprocessing import Pool,queues,Process,Queue

import os,time,random

def write(q):
    print('Process ti write: %s'%os.getpid())
    for value in ['a','b','c']:
        print('put %s to queue'%value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process ti read: %s'%os.getpid())
    while True:
        value = q.get(True)
        print('get %s from queue.'%value)

if __name__ == '__main__':
    #父进程创建queue，并传给各子进程：
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    #启动子进程跑完，写入
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    #等待pw结束
    pw.join()
    #pr进程就是死循环，无法等待其结束，只能强行终止
    pr.terminate()