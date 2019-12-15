# 异常处理,提前在代码里进行扑捉
try:
    """your code"""
except Exception:      #万能用法
    """出错后执行的代码"""

#万能异常
# while True:
#     try:
#
#         num1 =int(input("输入1"))
#         num2 =int(input("输入2"))
#
#         res = num1+num2
#         print("res",res)
#     except Exception as e:
#         print(e)
#值错误
# while True:
#     try:
#
#         num1 =int(input("输入1"))
#         num2 =int(input("输入2"))
#
#         res = num1+num2
#         print("res",res)
#     except ValueError as e:
#         print(e)
#命名错误
# while True:
#     try:
#
#         num1 =int(input("输入1"))
#         num2 =int(input("输入2"))
#
#         res = num1+num2
#         print("res",res,ne)
#     except NameError as e:
#         print(e)
while True:
    try:

        num1 =int(input("输入1"))
        num2 =int(input("输入2"))

        res = num1+num2
        print("res",res)
        # except Exception as e:
        #     print('万能错误')
    except NameError as e:
            print('命名异常')
    # except AttributeError as e:
    #         print("类没有属性")
    #     except ValueError as e:
    #         print("值错误")
    #     except IndentationError as e:
    #         print('缩进异常')
    #     except SyntaxError as e:
    #         print("语法错误")
    #     except IndexError as e:
    #         print("列表超出限制")
    #
    #     except (KeyboardInterrupt,EOFError) as e:
    #         print("键盘错误")
    #
    #     except TypeError as e:
    #         print("类型错误")
    #     except UnboundLocalError as  e:
    #         print("视图范围一个未设置的局部变量")