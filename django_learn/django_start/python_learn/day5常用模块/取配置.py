import configparser
config = configparser.ConfigParser()
# print(config.sections())

config.read('example.ini')#必须要先读取到配置
# print(config.sections())
# print(config['www.ser.com']['port'])

# for values in config['www.ser.com']:print(values)
sec = config.sections()
sec = config.remove_section('www.site.com')#删除配置
config.write(open('example.ini','w'))

sec = config.has_section('www.newsite.com')
# sec = config.add_section('www.newsite.com')#增加配置
# config.write(open('example.ini','w'))
# config.set('www.newsite.com','ke','122')
# config.write(open('example.ini','w')) #增加配置项中的值
config.remove_option('www.newsite.com','ke') #删除配置中的某个项
config.write(open('example.ini','w'))