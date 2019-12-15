def runnian():
    year = input("请输入要判断的年份\n")
    if int(year)%400 ==0:
        print("这是闰年")
    elif int(year)%4 ==0 and int(year)%100 !=0:
        print("这是闰年")
    else:
        print("这不是闰年")

runnian()