import asyncio
import time
import requests
async def request(url):
    print('正在请求的是',url)
    #当在asyncio中遇到阻塞操作必须手动进行挂起
    await asyncio.sleep(2)
    print('请求成功',url)
start = time.time()
urls =[
    'www.baidu.com',
    'www.sogou.com',
    'www.goubanjia.com'
]
stasks=[]
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    stasks.append(task)

loop = asyncio.get_event_loop()
#需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(stasks))
print(time.time()-start)