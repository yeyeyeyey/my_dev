import hashlib
md5 = hashlib.md5()
#md5,sha1算法的用法一致
md5.update('a new data'.encode('utf-8'))
print(md5.hexdigest())