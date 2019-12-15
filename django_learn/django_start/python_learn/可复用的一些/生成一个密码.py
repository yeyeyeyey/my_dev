import re
import hashlib
a = hashlib.md5()
a.update('dsds'.encode('utf-8'))
print(a.hexdigest())

def mima(salt='11'):
    pwd = input("请输入密码哦——需要包含字母数值")
    a = re.match('[a-z]',pwd)
    print(a)
    b = re.match('[0-9]+&',pwd)
    print(b)
    if a is None or b is None:
        print("需要包含数字+字母哦")
    else:
        pass
mima()