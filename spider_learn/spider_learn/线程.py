# import time
# def get_page(str):
#     print("正在下载：",str)
#     time.sleep(2)
#     print("下载成功",str)
# name = ['xiaozi','lele','meimei','wuzhong']
# start_time = time.time()
# for i in range(len(name)):
#     get_page(name[i])
# end_time = time.time()
# print("%d second"%(end_time - start_time))
import time
from multiprocessing.dummy import Pool
import time
start_time = time.time()
def get_page(str):
    print("正在下载：",str)
    time.sleep(2)
    print("下载成功",str)
name = ['xiaozi','lele','meimei','wuzhong']

# for i in range(len(name)):
#     get_page(name[i])

pool = Pool(4)
pool.map(get_page,name)
end_time = time.time()

print((end_time - start_time))
