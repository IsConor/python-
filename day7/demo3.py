'''
    函数:
        定义：用于封装一个特定的功能，表示一个功能或行为
        语法： def 函数名(形参):
        函数名：对函数体中语句的描述，规则与变量名相同
        返回值：方法定义者返回给调用者的结果
        作用域：local 函数内部   Global 全局  Enclosing 外部嵌套作用域：函数嵌套  Builtin 内置模块作用域：builtins.py文件
'''







# def buying():
#     def fun01(*args, **kwargs):
#         print(args)
#         print(kwargs)
#
#     fun01(1, 2, a=1)
#
#
# buying()

# # 查找空格
#
# str01 = " 校 训:自 强不西、厚德载物"
# print(str01.count(" "))
#
# # 删除前后空格
# str02 = str01.lstrip()
# str02 = str02.rstrip()
# print(str02)
# print(str01.replace(" ",""))
# print(str01.find("载物"))
# print(str01.startswith("校训"))



# def func07(a,b,*args,c,d,**kwargs):
#     pass
#
# func07(a=1, b=2, o=3,c=4, d=5, e=7,h=8)

# 定义数值相加的函数

# def add(*args):
#     num = 0
#     for item in args:
#         num += item
#     return num
# print(add(1,2,3,4))


# 星号元组形参： * 将所有实参合并为一个元组
# 作用：让实参个数无限制
# def fun02(*args):
#     print(args)
# fun02("a","b","c")


# 关键字形参
# def fun04(a, *args,b):
#     print(a)
#     print(b)
#     print(args)
#
# fun04(1,b=2)
# fun04(1,2,3,4, b=1)

# 双星号字典形参:
# ** 目的：将实参合并为字典，实参可以传递数量无限制的关键字实参
# def func06(**a):
#     print(a)
#
# func06(a=1,b=2)





# 定义函数，根据小时，分钟，秒，计算总秒数
# def clock(hours=0, min=0, sec=0):
#     return (hours * 3600 + min * 60 + sec)
#
# print(clock(min=5, sec=20))



# 函数参数 实际参数

# def func01(a,b,c,d):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#
# # 位置实参: 形参与实参的位置依次对应
# func(1,2,3,4)
#
# # 关键字实参
# func01(b=1,d=2,c=3,a=4)
#
# # 序列实参
# list01 = ["a","b","c","d"]
# func01(*list01) # *是将序列拆分后按位置与形参进行对应
#
# # 字典实参: ** 将字典拆分后按名称与形参进行对应
# dict01 = {"a":1,"c":2,"d":4,"b":2}
# func01(**dict01)



# 统计函数的执行次数

# num = 0
# def func01():
#     global num
#     num+=1
#
# func01()
# func01()
#
# print(num)


#
# # 定义判断列表中是否存在相同元素的函数
# def find_list_like(list_val):
#     '''
#         判断列表中是否存在相同元素
#     :param list_val: 列表
#     :return: True 或者 False
#     '''
#     for r in range(0, len(list_val)-1):
#         for c in range(r+1,len(list_val)):
#             if list_val[r] == list_val[c]:
#                 return True
#     return False
#
# list01 = [1, 2, 4, 3, 2, 9]
# print(find_list_like(list01))



# def level_num(number):
#     if number > 100 or number < 0:
#         return("输入有误")
#         return
#     if number > 90:
#         return "良好"
#     return "普通"
# print(level_num(97))


# # 定义计算四位整数，每位相加和的函数
# def each_unit_sum(val):
#     '''
#         计算整数的每位相加之和
#     :param val: 四位整数
#     :return: 四位整数相加之和
#     '''
#     result = val % 10
#     result += val // 10 %10
#     result += val // 100 % 10
#     result += val // 1000
#     return result
#
# print(each_unit_sum(1234))



# # 需求 两个数字相加的函数
# def sumval(val1, val2):
#     return val1 + val2
#
# print(sumval(1,2))



# 定义在控制台中打印二维列表的函数,倒置行和列

# def print_list(list_one):
#     #change_list(list_one)
#     for row in range(len(list_one)):
#         for col in range(len(list_one[row])):
#             print(list_one[col][row], end="\t")
#         print()
#
#
#
# list01 = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]
# ]
# print_list(list01)


# 在控制台中打印一维列表的函数
# def print_list(list_demo):
#     for item in list_demo:
#         print(item)
# list01 = [1,2,3,4,5]
# print_list(list01)


# def print_rectangle(row, col, char):
#     for r in range(row):
#         for c in range(col):
#             print(char, end=" ")
#         print()
#
# print_rectangle(33, 53, "%")