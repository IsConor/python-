
'''
    列表相关练习
    语句：
        循环语句：
            while -> 适用于根据条件循环
            for   -> 适用于根据次数循环
        容器：
            字符串str
                单引号，双引号，三引号
                转义字符
                格式化字符串
                通用操作：
                    + - * /  索引[]  切片[::]
                    in
            列表list
                由一系列变量组成的可变序列容器
'''
import random





# # 使用range生成5个1-10之间的数，将数字的平方存入list01中
# list01 = [random.randrange(1,10) **2 for item in range(5)]
# print(list01)
# # 将list01中所有奇数存入list02
# list02 = [item1 for item1 in list01 if item1 % 2 == 1]
# print(list02)
# # 将list01中所有偶数存入list03
# list03 = [item2 for item2 in list01 if item2 % 2 == 0]
# print(list03)
# # 将list01中所有偶数大于5的数字增加1后存入list04
# list04 = [item3 + 1 for item3 in list01 if item3 > 5 and item3 %2 == 0]
# print(list04)


# 列表推导式 --> 使用简易方法，将容器转化为列表
# list01 = [5, 56, 6, 7, 7, 8, 19]
# list02 = []
# for item in list01:
#     list02.append(item + 1)
# list02 = [item + 1 for item in list01 if item > 10]

# list02 = [item + 1 for item in list01]
# print(list02)


# 彩票由6个红球和1个蓝球组成，红球范围：  篮球范围： 系统随机生成一注号码
# 用户随机输入

# import random
#
# # 随机生成的彩票号码列表
# mylist = []
# while len(mylist) < 6:
#     num = random.randint(1,33)
#     if num not in mylist:
#         mylist.append(str(num))
#     else:
#         continue
# mylist.append(str(random.randint(1,16)))
#
# item = 0
# # 用户选择的彩票号码列表
# list_myinput = []
# while True:
#     if item == 6:
#         my_input = input("please input the blue number>")
#         if my_input == "":
#             break
#         elif int(my_input) < 1 or int(my_input) > 16:
#             print("不在号码范围内")
#             continue
#         elif my_input in list_myinput:
#             print("号码已经重复")
#             continue
#         list_myinput.append(my_input)
#         break
#     my_input = input("please input the %d red number>" %(item+1))
#     if my_input == "":
#         break
#     elif int(my_input) < 1 or int(my_input) >33:
#         print("不在号码范围内")
#         continue
#     elif my_input in list_myinput:
#         print("号码已经重复")
#         continue
#     list_myinput.append(my_input)
#     item += 1
#
# print("彩票中奖号码是：%s" %("".join(str(mylist))))
# print("你选择的号码是：%s" %("".join(str(list_myinput))))






# 练习：”How are you“ -> "you are How"
# 思路：将字符串转为列表，倒叙打印
# str01 = "How are you"
# list_01 = str01.split(" ")  #将字符串以空格拆分为列表
# print(" ".join(list_01[::-1])) #将列表取反转换成字符串




# 字符串转列表
# str01 = "张无忌-赵敏-周芷若"
# list_result = str01.split("-")
# print(list_result)


# 练习: 在控制台中循环输入字符串，如果输入空，则终止，最后打印所有内容
# str_list = []
# while True:
#     mystr = input("please input a str>")
#     if mystr:
#         str_list.append(str(mystr))
#     else:
#         break
# print("".join(str_list))


# 需求：根据xx逻辑，拼接一个字符串
# "0123456789"
# 优点：每次循环只需要向列表中添加字符串，没有创建列表对象
# list_temp = []
# for item in range(10):
#     list_temp.append(str(item))
# result = "".join(list_temp)
# print(result)
# join: list -> str


# 缺点：每次循环形成一个新字符串对象替换变量引用"result"
# result = ""
# for item in range(10):
#     result += str(item)
# print(result)




# 在列表[10, 25, 12, 8]中删除大于10的数字
# list01 = [9, 25, 12, 8]
# for item in range(len(list01)-1, -1, -1):
#     if list01[item] > 10:
#         del list01[item]
# print(list01)



# 在列表[54,25,12,42,35,17]，选出最大值
# list01 = [54,25,12,42,35,17]
# maxval = list01[0]  # 假设第一个是最大的
# for item in list01:
#     if item > maxval: # 与每个元素进行比较，如果发现更大的，则替换
#         maxval = item
# print(maxval)
# print(max(list01))


# 将列表[54,25,12,42,35,17]中大于30的数存入另外一个列表
# list01 = [54,25,12,42,35,17]
# list02 = []
# for item in list01:
#     if item > 30:
#         list02.append(item)
# print(list02)

# 在控制台中录入5个数字，打印最大值，不使用max
# maxstr = 0
# for item in range(1,6):
#     number = int(input("please input %d number > "%item))
#     try:
#         if number > maxstr:
#             maxstr = number
#     except ValueError:
#         print("you shuld input 5 number type = int")
# print(maxstr)


# 列表内存：

# 浅拷贝，不会复制深层变量绑定的对象
# list01 = [800, [1000,500]]
# # list02 = list01[:]
# list02 = list01.copy()
# list01[1][0] = 900
# print(list02[1][0]) # 900


# 深拷贝

# import copy
#
# list01 = [800, [1000,500]]
# list02 = copy.deepcopy(list01)
# list01[1][0] = 900
# print(list02[1][0])

# list01 = ["张无忌","赵敏"]
# list02 = list01
# list01[0] = "无忌"
# print(list02[0]) # 无忌

# list01 = ["张无忌","赵敏"]
# list02 = list01
# list01 = ["无忌"]
# print(list02[0]) # 张无忌



# 在控制台中录入所有学生的姓名，如果姓名重复，则提示已经存在，不再添加到列表中, 如果录入空字符串，则倒叙打印所有学生姓名
# str_name = []
# while True:
#     name = input("please input student' name>")
#     if name == "":
#         break
#     if name not in str_name:
#         str_name.append(name)
#     else:
#         print("姓名已存在，请勿重新录入")
# for i in range(len(str_name)-1, -1, -1):
#     print(str_name[i])



# 在控制台中录入所有学生成绩，输入空字符串，打印所有成绩,打印成绩最高分，打印最低分，打印平均分
# int_list = []
# while True:
#     number = input("please input student number>")
#     if number == "":
#         break
#     int_list.append(int(number))
# print("所有成绩")
# for i in int_list:
#     print("\t", i)
# print("最高分是：%d" %(max(int_list)))
# print("最低分是：%d" %(min(int_list)))
# print("平均分是：%.2f" %(sum(int_list) / len(int_list)))




# 1 在控制台中录入，在西游记中你喜欢的人物, 输入空字符串 打印所有（一行一个）人物


# print("在西游记中你喜欢的人物有：")
# list_n = []
# while True:
#     dem = input(">")
#     if dem == "":
#         break
#     list_n.append(dem)
# for item in list_n:
#     print(item)




# # 创建空列表
# list01 = []
# list01 = ()
#
# # 创建具有默认值的列表
# list02 = ["悟空", 100, True] #放数据
# list02 = list("我是齐天大圣") #放容器
#
# # 获取元素
# # 索引
# print(list02[2])
# # 切片
# print(list02[-4::])
#
# # 添加元素
# # 追加
# list02.append("八戒")
# print(list02)
# # 插入
# list02.insert(2,True)
# print(list02)
#
# # 删除元素
# # 根据元素删除
# list02.remove("是")
# print(list02)
# # 根据位置删除
# del list02[0]
# print(list02)
#
# # 定位元素 -> 增删改查
# # 切片
# del list02[1:3]
# print(list02)
# # [True, '大', '圣', '八戒']
# # [True, 'a', 'b', '八戒']
# list02[1:3] = ["a","b"]
#
# # [True, '八戒']
# list02[1:3] = []
# print(list02)
#
# # 遍历
# for item in list02:
#     print(item)
#
# # 倒叙遍历 -> 不建议 通过切片拿数据会重新创建新列表
# for item in list02[::-1]:
#     print(item)
#
# # 倒叙遍历所有元素
# for item in range(len(list02)-1,-1,-1):
#     print(list02[item])
#
# for item in range(-1, -len(list02)-1, -1):
#     print(list02[item])

# 输入宽和高 打印矩形

# wid = int(input("please input weight>"))
# hei = int(input("please input height>"))
#
# print(wid * "*")
# for i in range(0,hei-2):
#     print("*"+ " "*(wid-2) + "*")
# print(wid * "*")


# 在控制台获取一个字符串
# 打印第一个字符、最后一个字符、倒数第三个字符、前两个字符、倒叙打印所有字符，如果字符串长度是奇数，打印中间字符

# mystr = input("please input a number > ")
# print(mystr[0])     # 第一个字符
# print(mystr[-1])    # 最后一个字符
# print(mystr[-3])    # 倒数第三个字符
# print(mystr[0:3])   # 前两个字符
# print(mystr[::-1])  # 倒叙打印所有字符
# if len(mystr) % 2:
#     print(mystr[len(mystr) // 2])