#顺序查找，也叫线性查找，从列表第一个元素开始，顺序进行搜索，直到找到元素或搜索到列表最后一个元素为止。
#时间复杂度：O(n)
def linear_search(li,val):
    for ind,v in enumerate(li):
        if v==val:
            print(ind)
        else:
            print("没找到")
li = [1,3,4,6,4,52,7,3,8]

linear_search(li,6)