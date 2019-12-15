def select_sort_simple(li):
    for i in range(0,len(li)-1):
        min_log = i
        for j in range(i,len(li)):
            if li[j] <li[min_log]:
                min_log = j
        li[i],li[min_log] = li[min_log],li[i]
        print(li)
li = [234,1,43,6546,4645,2,235,543,62,5,34]
print(li)
select_sort_simple(li)
