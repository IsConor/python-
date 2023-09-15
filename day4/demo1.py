'''
    函数实现两个数值的除法计算
    异常捕获  --- try 被捕获的子语句   except (异常类型1, 类型2)   pass(忽略)
'''

def division(arg1, arg2):
    num = arg1 / arg2
    return num
try:
    num1 = int(input("please input arg1:"))
    num2 = int(input("please input arg2:"))

    num = int(division(num1, num2))
    print(num)
except ZeroDivisionError:
    print("除数不能为0")
except ValueError:
    print("please input int value")
except (EOFError, KeyboardInterrupt):
    pass