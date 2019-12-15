import pymysql
import  pymysql.cursors
# db = pymysql.connect(host = "localhost",user = "root",password = "lsj123456",
#                      db = "mysql",charset = "utf8mb4")
# cursor = db.cursor()
#
# cursor.execute("DROP TABLE IF EXISTS doubandb_movies")
# createTab = """create table doubandb_movies(
#     id INT PRIMARY KEY auto_increment,
#     title VARCHAR (100),score VARCHAR (10),info VARCHAR (100),movie_site
#     VARCHAR (100),pic_site VARCHAR (100),director VARCHAR (50),actor VARCHAR
#     (50),create_time datetime DEFAULT CURRENT_TIMESTAMP,update_time datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);"""
# cursor.execute(createTab)

import requests
# import urllib.request
# import urllib.parse
# import urllib.request,lxml.html
from bs4 import BeautifulSoup
import pymysql
import  pymysql.cursors
# db = pymysql.connect(host = "localhost",user = "root",password = "lsj123456",
#                      db = "mysql",charset = "utf8mb4")
# cursor = db.cursor()

def get_html():
    text = {}
    headers = {
        'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    url = 'https://weibo.com/u/2698634792'
    html = requests.get(url=url,headers=headers)
    # comment = BeautifulSoup(html, 'html.parser')
    print(html.text)
get_html()