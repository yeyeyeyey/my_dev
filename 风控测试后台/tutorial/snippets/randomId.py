# -*- coding: UTF-8 -*-

import random

def getRandom():
    head = random.randint(100000,999999)
    year = random.randint(1900,2019)
    month = random.randint(1,12)
    day = random.randint(1,31)
    tail = random.randint(1000,9999)

    if month == 2:
     if day > 28:
      day = 28

    daystr = ''
    if(day>10):
     daystr = str(day)
    else:
     daystr = '0'+str(day)

    monthstr = ''
    if(month>10):
     monthstr = str(month)
    else:
     monthstr = '0'+str(month)

    strId = str(head) + str(year) + monthstr + daystr + str(tail)
    print("身份证：" + strId)

    return strId
