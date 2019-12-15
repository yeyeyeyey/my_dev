# from multiprocessing import Process
# import os
#
# def run_proc(name):
#     print('run child process %s (%s)'%(name,os.getpid()))
#
#
# if __name__ == '__main__':
#     print('Parent process %s' %os.getpid())
#     p =Process(target=run_proc,args=('test_open',))
#     print('child start')
#     p.start()
#     p.join()
#     print('child end')
#多个进程可以表示为人左手画圆，右手画方 ，两只手相当于两个进程
import multiprocessing
import time
def action(a,b):
    for i in range(10):
        print(a,b,"冇内鬼，GKD")
        time.sleep(1)

def act(a,b):
    for i in range(10):
        print(a,b,"有内鬼，停止交易")
        time.sleep(1)
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=act,args=('有内鬼','内鬼渣渣辉'))
#     p2 = multiprocessing.Process(target=action,args=('没有内鬼','去送龙头棍'))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print('交易完成了么')
#     p1.close()
#     p2.close()
#queue表示进程之间的通信
def foo(a):
    s = a.get()
    print('警察已收到数据')
    print(s)

if __name__ == '__main__':
    tx = multiprocessing.Queue()#创建进程通信的queue
    jc = multiprocessing.Process(target=foo,args=(tx,))
    jc.start()
    print('开始准备交易')
    tx.put('被抓到了，你们有内鬼')
    jc.join()