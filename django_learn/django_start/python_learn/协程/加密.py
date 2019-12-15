import hashlib
# a = hashlib.sha256('222').encode('utf-8')
# print(a)

def jiami(s,salt = 'salt'):
    md5 = hashlib.md5()
    md5.update((s+salt).encode('utf-8'))
    return md5.hexdigest()

print(jiami('2'))



def login(user,password):
    user = input("请输入用户名\n")
    password = input("请输入密码\n")
