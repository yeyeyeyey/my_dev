# #列表每两个相邻的数，如果前面两个比后面大，则交换这两个数
# import random
#
# def bubble_sort(li):
#     for i in range(len(li)-1):
#         for j in range(0,len(li)-i-1):
#             if li[j] > li[j+1]:
#                 li[j],li[j+1] = li[j+1],li[j]
#
# li = [random.randint(1,1000) for i in range (100)]
#
# print(li)
#
# bubble_sort(li)
# print(li)
#
import random
# def maopao(li):
#     for i in range(len(li)-1):
#         for j in range(0,len(li)-i-1):
#             if li[j]>li[j+1]:
#                 li[j],li[j+1] = li[j+1],li[j]
#         print(li)
# li = [23,645,6,3,65,85,25,756,8]
# phone_num = [random.randint(10000000,99999999) for i in range(9)]
# a = ''
# phone = a.join('%s' %i for i in phone_num)
# print(type(phone))
# (maopao(li))
# print(li)







def maopao(li):
    for i in range(0,len(li)-1):
        for j in range(0,len(li)-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]

li = [23,645,6,3,65,85,25,756,8]
maopao(li)

print(li)








