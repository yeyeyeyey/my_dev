import  time
import threading

def addNum():
    global num
    print('-- get num--',num)
    time.sleep(1)
    num -=1

num = 100

thread_list = []
for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list:
    t.join()

print('final num:',num)


#python3现在回自动锁线程，当一个线程运行时，其他人都不能动