import requests
import json
#UA伪装
#UA检测，
# User-agent（请求载体的身份标识）
if __name__ == '__main__':
    url = 'https://fanyi.baidu.com/sug'

    headers = {
        'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    kw = input('enter a word:')
    data = {
        'kw':kw
    }
    # param = {
    #     'query':kw
    # }
    response = requests.post(url=url,data=data,headers = headers)
    # page_text = response.text
    j = response.json()
    # fileName = kw+'.html'
    # with open(fileName,'w',encoding='utf-8') as fp:
    #     fp.write(page_text)
    # print(fileName,"保存成功！")
    # print(j)
    # fp = open('./dog.json','w',encoding='utf-8')
    # json.dump(j,fp = fp,ensure_ascii=False)
    print(j)
    print('over!')