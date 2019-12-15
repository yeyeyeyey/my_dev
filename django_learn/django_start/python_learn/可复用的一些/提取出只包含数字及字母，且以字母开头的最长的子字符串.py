testStr = '2kd4-1124*2|^2sdAmZ%fkMcv'
list=[]
for i in testStr:
    list.append(i)
list.sort()
list.reverse()
dic = {}
for k,v in enumerate(list):
    dic[k]=v
print(dic)