def quicksort(li):
    if len(li) >=2:
        mid = li[len(li)//2]
        left,right = [],[]
        li.remove(mid)
        for i in li:
            if i >=mid:
                right.append(i)
            elif i <mid:
                left.append(i)
        return quicksort(left) + [mid] + quicksort(right)
    else:
        return li
# def quick_sort(data):
#     """快速排序"""
#     if len(data) >= 2:  # 递归入口及出口
#         mid = data[len(data)//2]  # 选取基准值，也可以选取第一个或最后一个元素
#         left, right = [], []  # 定义基准值左右两侧的列表
#         data.remove(mid)  # 从原始数组中移除基准值
#         for num in data:
#             if num >= mid:
#                 right.append(num)
#             else:
#                 left.append(num)
#         return quick_sort(left) + [mid] + quick_sort(right)
#     else:
#         return data
print(quicksort([1,345,53,4,44233,34,23,5,32,324,123,4324]))
# a=[1,2,3]
# b=[4,332,4]
# print(a+b)