import threading,time,random
#任何进程启动后都会启动一个线程
def loop():
    print('threading %s is running...'%threading.current_thread().name)
    n = 0
    while n<6:
        n +=1
        print('threading %s is running...' % threading.current_thread().name)
        time.sleep(1)
    print('threading %s  end...' % threading.current_thread().name)


print('threading %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop,name='线程1')
t.start()
t.join()
print('threading %s end...' % threading.current_thread().name)
