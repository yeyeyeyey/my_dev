import requests
#UA伪装
#UA检测，
# User-agent（请求载体的身份标识）
if __name__ == '__main__':
    url = 'https://www.sogou.com/web'
    headers = {
        'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    kw = input('enter a word:')
    param = {
        'query':kw
    }
    response = requests.get(url=url,params=param,headers = headers)
    page_text = response.text
    fileName = kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,"保存成功！")