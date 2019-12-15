# 协程在同一线程执行，协程性能优势，不需要多线程的锁机制，不存在写变量冲突，在协程中控制共享资源不加锁
# 协程只是一个线程执行。
# 如果利用多核cpu，多进程+协程
# python对协程的支持是通过generator实现的！！！！！！！！！！！！
import os
def consomer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[consumer] consuming %s'%n)
        r = '200ok'

def produce(c):
    c.send(None)
    n = 0
    while n<5:
        n=n+1
        print('[producer] producing %s...'%n)
        r = c.send(n)
        print('[producer] consumer return: %s'%r)
    c.close()

c = consomer()
produce(c)

# 注意到consumer函数是一个generator，把一个consumer传入produce后：
#
# 首先调用c.send(None)启动生成器；
#
# 然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
#
# consumer通过yield拿到消息，处理，又通过yield把结果传回；
#
# produce拿到consumer处理的结果，继续生产下一条消息；
#
# produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
#
# 整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
#
# 最后套用Donald Knuth的一句话总结协程的特点：
#
# “子程序就是协程的一种特例。”
print(os.path)