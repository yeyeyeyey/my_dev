def midfen(li,val):
    left = 0
    right = len(li)
    while left <=right:
        mid = (left+right)//2
        if li[mid] == val:
            return mid
        elif li[mid]>val:
            right = mid -1
        else:
            left = mid +1


li = [1,2,5,645,3453,645656,234245645646]
print(midfen(li,645))