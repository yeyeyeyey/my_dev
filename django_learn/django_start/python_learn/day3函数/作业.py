info = {"id":1,"name":'lsj','age':22,"job":'it',"time":'2019'}
def select(s,*args):
    return info.get(s),info.get(args)

print(select('id'))