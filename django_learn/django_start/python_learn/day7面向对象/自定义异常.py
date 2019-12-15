#自己定义一个类
class MyException(BaseException):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

# 万能异常一般放在异常后面
while True:
    try:

        num1 =int(input("输入1"))
        num2 =int(input("输入2"))

        res = num1+num2
        print("res",res)
        raise MyException('那里不可以')
        # raise ValueError   #主动触发异常，便于手动触发异常
        # except Exception as e:
        #     print('万能错误')

    except NameError as e:
        print('命名异常')
    except MyException as e:
        print("不能哦",e)
    else:
        print("没发生异常走这里")
    finally:
        print("不管有没有异常，都要走这里")

#

#自定义异常

