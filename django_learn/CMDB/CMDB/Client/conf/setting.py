import os
#远端接受数据的服务器
Params = {
    'server':'10.3.208.68',
    'port':8000,
    'url':'/assets/report/',
    'request_timeout':30,
}
#日志文件配置
PATH  = os.path.join(os.path.dirname(os.getcwd()),'log','cmdb.log')
# 这里，配置了服务器地址、端口、发送的url、请求的超时时间，以及日志文件路径。请根据你的实际情况进行修改。