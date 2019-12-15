import pymysql
import  pymysql.cursors
db = pymysql.connect(host = "localhost",user = "root",password = "lsj123456",
                     db = "mysql",charset = "utf8mb4")
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS doubandb_movies")
createTab = """create table doubandb_movies(
    id INT PRIMARY KEY auto_increment,
    title VARCHAR (100),score VARCHAR (10),info VARCHAR (100),movie_site 
    VARCHAR (100),pic_site VARCHAR (100),director VARCHAR (50),actor VARCHAR 
    (50),create_time datetime DEFAULT CURRENT_TIMESTAMP,update_time datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);"""
cursor.execute(createTab)


import urllib.request
import urllib.parse
import urllib.request,lxml.html
from bs4 import BeautifulSoup
import pymysql
import  pymysql.cursors
db = pymysql.connect(host = "localhost",user = "root",password = "lsj123456",
                     db = "mysql",charset = "utf8mb4")
cursor = db.cursor()

class Get_book(object):
    # def __init__(self,url):
    #     self.url = url
        # self.book = book
        # self.field = field
    def get_html(self):
        # url = self.url
        # html = urllib.request.urlopen(url).read().decode('utf-8')
        # moviesoup = BeautifulSoup(html,'html.parser')

        for i in range(0, 10):
            movie = {}
            url = 'https://movie.douban.com/top250?start={}&filter='.format(i)
            html = urllib.request.urlopen(url).read().decode('utf-8')
            moviesoup = BeautifulSoup(html, 'html.parser')
            for item in moviesoup.find_all(class_ = 'item'):
                title = item.find(class_='title').get_text()
                score = item.find(class_ ='rating_num').get_text()
                info = item.find(class_ = 'inq').get_text()
                pic_site = item.find(class_ = 'pic').find('a').find('img')['src']
                movie_site = item.find(class_ = 'hd').find('a')['href']
                person_info = item.find(class_ = 'info').find(class_ = 'bd').find(
                    'p').get_text().strip().split('\n')[0]
                director = person_info.split('\xa0\xa0\xa0')[0][3:]
                actor = person_info.split('\xa0\xa0\xa0')[1][3:]
                movie['title'] = title
                movie['score'] = score
                movie['info'] = info
                movie['movie_site'] = movie_site
                movie['pic_site'] = pic_site
                movie['director'] = director
                movie['actor'] = actor
                sql = "INSERT INTO  doubandb_movies (title,score,info," \
                      "movie_site,pic_site," \
                      "director,actor) VALUES (%s,%s,%s,%s,%s," \
                      "%s,%s)"
                cursor.execute(sql, (movie['title'], movie['score'], movie['info'],
                                     movie['movie_site'], movie['pic_site'],
                                     movie['director'],
                                     movie['actor']))
                db.commit()
                print("成功插入数据！")
            # # return (movie)
                print(movie)
#
# for i in range(0,10):
#     url = 'https://movie.douban.com/top250?start={}&filter='.format(i)

a= Get_book()
b=a.get_html()
# print(b)
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


