def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dic = {}
    for index, value in enumerate(nums):
        dic[value]=index
        # print(type(index),type(value))
        # another_value =target-value
        # if another_value in nums:
        #     print(dic[another_value])
        print(dic)
        another = target-value
        if another in dic:
            print(dic[another],index)

twoSum([1,24,6,3,2,5],7)


