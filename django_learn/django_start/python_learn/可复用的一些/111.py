def romanToInt( s):
    """
    :type s: str
    :rtype: int
    """
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    w = 0
    a = list(dic.keys())
    # print(a)
    # print(list[dic.keys()][1])
    d = {}
    for k, v in enumerate(s):
        d[k]=v
        # print(d)
        if v in a:

            w += int(dic[v])
    print( w)

romanToInt("IMXV")