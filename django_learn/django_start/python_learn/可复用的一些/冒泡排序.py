# def maopao(li):
#     a = len(li)
#     for i in range(0,a):
#         for j in range(0,a-i-1):
#             if li[j] > li[j+1]:
#                 li[j],li[j+1]=li[j+1],li[j]
#
# li=[1,435,63,23,4,2]
# # maopao(li)
# print(li[::])
# li.append([3])
# # print(li)

def exep(v,list=[]):
    list.append(v)
    return list
list1 = exep(10)
list2 = exep(123,[])
list3 = exep('a')
assert(list1, [10])
assert( list2, [123])
assert( list3, ['a'])
# print(list1)