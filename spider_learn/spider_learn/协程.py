import time
def producer():
    g = consumer()
    next(g)
    for i in range(10000000):
        g.send(i)

def consumer():
    while True:
        res = yield
start_time = time.time()


producer()

end_time = time.time()
print(end_time-start_time)

import time
def producer():
    res = []
    for i in range(10000000):
        res.append(i)
    return res

def consumer(res):
    pass
start_time = time.time()

consumer(producer())

end_time = time.time()
print(end_time-start_time)