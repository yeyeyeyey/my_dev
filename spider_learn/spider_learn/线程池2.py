import requests
from lxml import html
import re
from multiprocessing.dummy import Pool

headers = {
    'User-agent' :'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
url = 'https://www.pearvideo.com/category_5'

page_text = requests.get(url=url,headers = headers).text

etree = html.etree

tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id = "listvideoListUl"]/li')
# print(li_list)
for li in li_list:
    detail_url = 'https://www.pearvideo.com/'+li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/text()')[0]+'.mp4'
    urls = []
    #对详情页的url进行请求
    detail_url_text = requests.get(url=detail_url,headers=headers).text
    ex = 'srcUrl="(.*?)",vdoUrl'
    video_url = re.findall(ex,detail_url_text)[0]
    # print(detail_url,name)
    # print(video_url)
    # urls.append(video_url)
    dic = {
        'name':name,
        'url':video_url
    }
    urls.append(dic)
    # print(dic)
def get_video_data(dic):
    url = dic['url']
    print(dic['name'],'正在下载')
    data = requests.get(url= url,headers=headers).content
    with open(dic['name'],'wb') as fp:
        fp.write(data)
        print(dic['name'],'下载成功')
pool = Pool(4)
pool.map(get_video_data,urls)
pool.join()