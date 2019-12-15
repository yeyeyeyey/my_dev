import configparser

config = configparser.ConfigParser()
config['DEFAULT'] ={
     'name':'lsj',
     'age':25,
     'sex':"male"
}
config['www.site.com']  = {}
config['www.ser.com'] = {}
topsecret = config['www.ser.com']
topsecret['port'] = '443'
topsecret['database'] = 'mysql'
with open('example.ini','w') as conf:
    config.write(conf)