
import requests
import urllib.request
import urllib.parse
import urllib.request,lxml.html
from bs4 import BeautifulSoup
from lxml import html
text = ''
etree = html.etree

if __name__ == '__main__':
    url = 'https://movie.douban.com/top250?start={}&filter='
    headers = {
        'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    page_data = requests.get(url=url,headers=headers).text
    moviesoup = BeautifulSoup(page_data, 'html.parser')
    for item in moviesoup.find_all(class_ = 'item'):
        pic_site = item.find(class_ = 'pic').find('a').find('img')['src']
        
        with open('./爬取图片/douban_pic','w',encoding='utf-8') as fp:
            fp.write()
        print(pic_site)
# class Get_book(object):
#     # def __init__(self,url):
#     #     self.url = url
#         # self.book = book
#         # self.field = field
#     def get_html(self):
#         # url = self.url
#         # html = urllib.request.urlopen(url).read().decode('utf-8')
#         # moviesoup = BeautifulSoup(html,'html.parser')
#
#         for i in range(0, 10):
#             movie = {}
#             url = 'https://movie.douban.com/top250?start={}&filter='.format(i)
#             html = urllib.request.urlopen(url).read().decode('utf-8')
#             moviesoup = BeautifulSoup(html, 'html.parser')
#             for item in moviesoup.find_all(class_ = 'item'):
#                 title = item.find(class_='title').get_text()
#                 score = item.find(class_ ='rating_num').get_text()
#                 info = item.find(class_ = 'inq').get_text()
#                 pic_site = item.find(class_ = 'pic').find('a').find('img')['src']
#                 movie_site = item.find(class_ = 'hd').find('a')['href']
#                 person_info = item.find(class_ = 'info').find(class_ = 'bd').find(
#                     'p').get_text().strip().split('\n')[0]
#                 director = person_info.split('\xa0\xa0\xa0')[0][3:]
#                 actor = person_info.split('\xa0\xa0\xa0')[1][3:]
#                 movie['title'] = title
#                 movie['score'] = score
#                 movie['info'] = info
#                 movie['movie_site'] = movie_site
#                 movie['pic_site'] = pic_site
#                 movie['director'] = director
#                 movie['actor'] = actor
#             # # return (movie)
#                 print(pic_site)
# #
# # for i in range(0,10):
# #     url = 'https://movie.douban.com/top250?start={}&filter='.format(i)
#
# a= Get_book()
# b=a.get_html()
# # print(b)
#     sql = "INSERT INTO  doubandb_movies (title,score,info," \
#       "movie_site,pic_site," \
#    "director,actor) VALUES (%s,%s,%s,%s,%s," \
#       "%s,%s)"
#     cursor.execute(sql,(b['title'],b['score'],b['info'],
#                         b['movie_site'],b['pic_site'],b['director'],
#                         b['actor']))
#     db.commit()
#     print("成功插入数据！")
   #  db.close()
   #  print(b)
# //*[@id="main"]/div[3]/div[2]/ul/li[7]/a
# //*[@id="main"]/div[4]/div[2]/ul/li[5]/a
# //*[@id="hotcontent"]/div[1]/div[1]/dl/dt/a
# //*[@id="wrapper"]/div[3]/ul/li[3]/a
# //*[@id="wrapper"]/div[3]/ul/li[7]/a
# results = re.findall('<li.*?>.*?(.*?<a.*?singer=".*?">)?(<i.*?></i>)?(.*?)(</a>.*?)?</li>',html,re.S)


