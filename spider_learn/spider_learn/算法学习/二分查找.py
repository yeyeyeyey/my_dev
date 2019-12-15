# #二分查找，又叫折半查找，从有序列表的初始候选区li[0:n]开始，通过对待查找的值与候选区中间值的比较，可以使候选区减少一半
#
# def binary_search(li,val):
#     left = 0
#     right = len(li) -1
#     while left<=right:      #候选区有值
#         mid = (left+right)//2
#         if li[mid] ==val:
#             return " 这是第 %d 个值 " %(mid+1)
#         elif li[mid]>val:   #待查找的值在mid左侧
#             right = mid -1
#         else:       #li[mid]<val 待查找的值在mid右侧
#             left = mid+1
#     # return None
#
# li = list(range(1,100))
# a=binary_search(li,11)
# print(a)
# def binary_search(data_list, target):
#     """
#     :param data_list: 传入的有序列表
#     :param target:  传入要查找的目标值
#     """
#     low = 0  # 最小数下标
#     high = len(data_list) - 1  # 最大数的下标
#     index = 1  # 用index来记录查找的次数
#
#     while low <= high:
#         mid = (low + high) // 2  # 取中间值
#
#         if data_list[mid] == target:
#             return "一共查找了%d次,此数字在列表中的下标为:%d" % (index, mid)
#         elif data_list[mid] > target:
#             high = mid - 1  # 如果中间值比目标值大,则在mid左半边找
#         else:
#             low = mid + 1  # 如果中间值比目标值小,则在mid右半边找
#
#         index += 1
#     return "一共找了%d次,找不到这样的值!" % index
#
#
# ret1 = binary_search(list(range(1, 1000)), 888)
# ret2 = binary_search(list(range(1, 1000)), 10000)
# print(ret1)
# print(ret2)



def binary_search(li,val):
    left = 0
    right = len(li)
    while left <= right:
        mid = (left+right)//2
        if li[mid] ==val:
            return '这是第 %d个值' %(mid+1)
        elif li[mid]>val:
            right = mid -1
        else:
            left = mid +1
li = [1,2,55,76,8768,34535,3553453]

print(binary_search(li,55))