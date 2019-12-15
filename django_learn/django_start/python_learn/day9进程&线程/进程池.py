from multiprocessing import Pool

import os,time,random

def long_time_task(name):
    print('run task %s on (%s)'%(name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    take_time  = end - start
    print('Task %s cost %f second'%(name,take_time))

if __name__ == '__main__':
    print('Parent process %s'%os.getpid())
    p  = Pool(10) #选择自己想要的进程数
    for i in range(10):
        p.apply_async(long_time_task,args=(i,))
    print('wait for success')
    p.close()
    p.join()
    print('all ok')