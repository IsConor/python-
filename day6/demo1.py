'''
    数据的类型转换
    运算符
        算数运算符 +  -  *  /  //  %  **
        增强运算符 +=  -=  *=  /=  //=  %=  **=
        比较运算符 > < >=  <=  ==  !=  结果是bool类型：True  False
        逻辑运算符 and  or
'''

# 随机产生两个数字（1~10），在控制台中获取两个数相加的结果，若用户输入正确得10分

# import random
#
# a = 0
# for i in range(3):
#     number1 = random.randint(1, 10)
#     number2 = random.randint(1, 10)
#     sum = number1 + number2
#     result = input("%d + %d = ?" %(number1, number2))
#     if int(result) == sum:
#         print("+10")
#         a += 10
#     else:
#         print("error, %d again" %(2-i))
#         continue
#
# print("good, you have %d" %(a))




# 累加10~36之间的和
# sum = 0
# for i in range(10, 37):
#     sum += i
# print(sum) #621

# 累加1~100之间的偶数和
# sum = 0
# for i in range(2, 101, 2):
#     sum += i
# print(sum) #2550

# 累加1~100的和

# num = 0
# for i in range(1, 101):
#     num += i
# print(num)



# for 循环 range 更善于设定循环次数
#
# for i in range(1,10):
#     print(i)



# 游戏运行产生1~100的随机数，让玩家重复猜测，直到猜对为止

# import random
#
# c_number = random.randint(1,100)
# i = 0
# while i < 10:
#     i+=1
#     u_number = int(input("please input a num >"))
#     if u_number > c_number:
#         print("too big")
#     elif u_number < c_number:
#         print("too small")
#     else:
#         print("you win")
#         break
# if i== 10:
#     print("you lose")


# 一张纸的厚度为0.01毫米，计算对折多少次，超过珠穆朗玛峰8844.43米

# paper = 0.01 / 1000  # 1米 = 1000毫米
# number = 0
# while paper <= 8844.43:
#     paper *= 2
#     number += 1
#
# print(number)


# 一次 0.01 * 2
# 两次 0.01 * 2**2
# 三次 0.01 * 2**3
# n次 0x01 * 2** n


# 在控制台中获取一个开始值， 一个结束值，将中间的数字打印出来，例如开始值为3，结束值为10，打印456789
# begin = int(input("please input begin number >"))
# end = int(input("please input end number >"))
# while True:
#     begin+=1
#     print(begin)
#     if begin == end -1:
#         break


# 练习1 在控制台中获取一个整数，如果是偶数，给变量num赋值”偶数" , 否则赋值 "奇数"
# num = "奇数" if int(input("please input a num >")) % 2  else "偶数"
# print(num)




# 真值表达式

# str_input = input("please input a num >")
# if str_input:
#     print("input success")
#
# # 条件表达式
# sex = None
# if input("please input sex >") == "man":
#     sex = 1
# else:
#     sex = 0
#
# sex = 1 if input("please input sex >") == "man" else 0

# a = 1000
# d = 1000
# print(a is d)
#



# 身份运算符 x is not y
# a = "800"
# b = "1000"
# # id 函数可以获取变量存储的地址
# print(id(a))
# print(id(b))
# print(a is b)   #false
# print(a is not b) #true
#


# del
# a = "tom"
# b = a
# c = a
# # 删除变量a b，不释放对象
# del a, b
# # 由于变量d不再引用对象"tom"， tom的引用计数为0，所以对象"tom"被标记为可销毁
# d = None

# print(a)

# def func(num):
#     one = num % 10
#     two = (num // 10) % 10
#     three = (num // 100) % 10
#     four = (num // 1000)
#     print(one + two + three + four)
#
# number = int(input("please input four num > "))
#
# func(number)