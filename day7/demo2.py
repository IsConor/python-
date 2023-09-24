'''
    字典推导式
    集合 set
        由一系列不重复的不可变类型变量组成的可变映射容器，相当于只有键的字典
'''









# 定义方阵转置函数

# def change_list(list_demo):
#     for row in range(1, len(list_demo)):
#         for col in range(row, len(list_demo)):
#             list_demo[row-1][col], list_demo[col][row-1] = list_demo[col][row-1], list_demo[row-1][col]
#
# list01 = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
# change_list(list01)
# change_list(list01)
# print(list01)



# 定义列表升序排列的函数

# def list_sort(list_a):
#     '''
#         将列表中的数据进行升序排列
#     :param list_a: 整型列表
#     :return:None
#     '''
#     for row in range(0, len(list_a)):
#         for col in range(row+1, len(list_a)):
#             if list_a[row] > list_a[col]:
#                 list_a[row], list_a[col] = list_a[col], list_a[row]
#
#
# list01 = [1,4,43,2,31,3]
# list_sort(list01)
# print(list01)







# python函数在调用时开辟内存到栈帧，调用结束之后会释放空间

# 可变与不可变类型在传参时
    #不可变类型的数据在传参时，函数内部不会改变源数据的值
    #可变类型的数据在传参时，函数内部可以改变源数据的值




# 列表全排列
# list01 = ["苹果", "香蕉", "哈密瓜"]
# list02 = ["可乐", "牛奶"]
# print(set(list01) | set(list02)) # {'牛奶', '苹果', '可乐', '香蕉', '哈密瓜'}
# list03 = [row+col for row in list01 for col in list02 ] #['苹果可乐', '苹果牛奶', '香蕉可乐', '香蕉牛奶', '哈密瓜可乐', '哈密瓜牛奶']
# print(list03)



# list01 = ["a", "b", "c"]
# list02 = ["A", "B", "C"]
# list03 = []
# for row in list01:
#     for col in list02:
#         list03.append(row+col)
# print(list03)
#
# list04 = [row + col for row in list01 for col in list02]
# print(list04)


# 矩阵转置  将二维列表的列变成行
# list01 = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]
# ]
#
# list02 = []
# for row in range(len(list01)):
#     list_emp = [list01[col][row] for col in range(len(list01[row]))]
#     list02.append(list_emp)
# print(list02)



# list01 = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]
# ]
# # 打印第二行第三个元素
# que = [{"练习1":0, "练习2":[], "练习3":[]}]
# list02 = []
# for row in range(len(list01)):
#     for col in range(len(list01[row])):
#         if row == 2 and col == 3:
#             que[0]["练习1"] = list01[row-1][col-1]
#         if row == 3:
#             que[0]["练习2"] = list01[row-1]
#         if col == 1:
#             list02.append(list01[row][col-1])
#             que[0]["练习3"] = list02
#
# for key, value in que[0].items():
#     print("%s的结果 "%(key)+str(value))




# 判断列表中元素是否有相同的
# result = False
# list01 = [3, 80, 45, 5, 80]
# for row in range(len(list01)): # 循环5次
#     for col in range(row+1, len(list01)): #循环4次
#         if list01[row] == list01[col]:
#             print("有相同的%d=%d" % (list01[row], list01[col]))
#             result = True
#             break
#     if result:
#         break
# if result == False:
#     print("没有相同的")


# 排序
# list01 = [3, 80, 4, 45, 5, 7, 1, 100, 2]
# for row in range(len(list01) - 1):
#     for col in range(row+1, len(list01)):
#         if list01[row] < list01[col]:
#             list01[row], list01[col] = list01[col], list01[row]
# print(list01)

# for item in range(4):
#     for r in range(item+1):
#         print("*", end=" ")
#     print()


# for r in range(4):
#     for c in range(3):
#         print("*#", end="")
#     print()


# # 固定集合
# set01 = frozenset((1, 2, 3, 4, 43, 5))
# print(set01)


# 在控制台中循环录入字符串，输入空字符停止，打印所有不重复的文字
# set01 = set()
# while True:
#     str01 = input("please input a val >")
#     if str01 == "":
#         break
#     set01.add(str01)
# print(list(set01 & set01))

# 经理：曹操，刘备，孙权 技术：曹操，刘备，张飞 关羽， 请计算：1是经理也是技术的有？  2是经理不是技术的有？
# 3是技术 不是经理的有？  4 张飞是经理吗？ 5 身兼一职的都有？ 6 经理和技术总共有多少人
# set01 = {"曹操", "刘备", "孙权"}
# set02 = {"刘备", "曹操", "关羽", "张飞"}
# que01 = set(set01 & set02)
# que02 = set((set01 | set02) ^ set02) # set(set01 - set02)
# que03 = set((set01 | set02) ^ set01) # set(set02 - set01)
# que04 = set(set01 ^ set02)
# que05 = len(set(set01 | set02))
# print("是经理也是技术的有 %s" %(" ".join(que01)))
# print("是经理不是技术的有 %s" %(" ".join(que02)))
# print("是技术不是经理的有 %s" %(" ".join(que03)))
# print("张飞是经理码？" + str(set("张飞") < set01))
# print("身兼一职的有 %s" %(" ".join(que04)))
# print("一共有%d人"%que05)

# # 数学运算
# set01 = {1, 2, 3}
# set02 = {2, 3, 4}
#
# # 交集
# print(set01 & set02) #{2, 3}
#
# # 并集
# print(set01 | set02) #{1, 2, 3, 4}
#
# # 补集
# print(set01 ^ set02) #{1, 4}
#
# # 子集
# set03 = {1, 2}
# print(set03 < set01) # True
#
# # 超集
# print(set01 > set03) # True




# # 1 创建空集合  集合名 = set()  /  集合名 = set(可迭代对象)
# set01 = set()
#
# # 2 创建具有默认值的集合  集合名 = {1，2，3}  /  集合名 = set(可迭代对象)
# set01 = set("abccd")
# str01 = "".join(set01) # 切换回字符串
# tuple01 = tuple(set01) # 切换为元组
#
# # 3 添加元素  集合名.add(元素)
# set01.add("qtx")
# print(set01)
#
# # 4 删除元素  集合名.discard(元素)
# set01.remove("a")
# print(set01)
#
# # 5 获取所有元素
# for item in set01:
#     print(item)






# # 需求：字典如何根据值查找键
# # 方案一：键值互换  ， 缺点：如果key重复，则丢失数据 {'无忌': 101, '赵敏': 101, '周芷若': 103}
# dict01 = {'无忌': 101, '赵敏': 101, '周芷若': 103}
# dict02 = { value:key for key, value in dict01.items() }
# print(dict02[101])
#
# # 方案二： 将字典转化为列表，将key和value封装为元组
# list02 = [(key,value) for key, value in dict01.items()]
# print(list02)


# 推导式应用
# {'无忌': 2, '赵敏': 2, '周芷若': 3}
# list_name = ["无忌","赵敏", "周芷若"]
# item_name = {item:len(item) for item in list_name}
# print(item_name)


# [101, 102, 103]
# {"无忌":101, "赵敏":102, "周芷若":103}
# list_rome = [101, 102, 103]
# item_rome = {list_name[item]:list_rome[item] for item in range(len(list_name))
#              if len(list_name) == len(list_rome)}
# print(item_rome)

# 1 2 3 4 .... 10 -> 平方
# dict01 = {}
# for item in range(1,11):
#     dict01[item] = item ** 2
# print(dict01)
#
# # 推导式
# dict02 = {item: item ** 2 for item in range(1,11)}
# print(dict02)
#
# # 推导式 + 条件
# dict02 = {item:item ** 2 for item in range(1,11) if item > 5}


# 计算一个字符串中的字符以及出现的次数
# abccdefg  [a,b,c,c,d,e,f,g]
# list01 = ["a","b","c","c","d","e","f","g"]
# print(list01.count("c"))

# demo = input("please input str>")
# list_demo = [item for item in demo]
# dict_demo = dict()
#
# # 将列表中的每个元素作为键，元素出现的数量作为值存入字典
# list01 = [] # 存放键
# for item in list_demo:
#     if item not in list01:
#         list01.append(item)
# list_value = [list_demo.count(item) for item in list01]
#
# for item in range(len(list01)):
#     dict_demo[list01[item]] = list_value[item]
# for key, value in dict_demo.items():
#     print("%s 出现了 %d 次" %(key, value))


# 存储全国各个城市的景区与美食，在控制台中显示出来
# 北京：
    #景区：故宫、天安门、天坛
    #美食：烤鸭、炸酱面、豆汁、卤煮
# 四川：
    #景区：九寨沟、峨眉山、春熙路
    #美食：火锅、串串香、兔头
# 思路：
#[ {北京:[美食[]，景区[]], 四川:[美食[]，景区[]]} ]
# list_demo = []
# list_beijing_meishi = ["烤鸭","炸酱面","豆汁","卤煮"]
# list_beijing_jingqu = ["故宫","天安门","天坛"]
# list_beijing = [list_beijing_jingqu, list_beijing_meishi]
#
# list_sichuan_meishi = ["火锅","串串香","兔头"]
# list_sichuan_jingqu = ["九寨沟","峨眉山","春熙路"]
# list_sichuan = [list_sichuan_jingqu, list_sichuan_meishi]
# dict_country = {"北京":list_beijing, "四川":list_sichuan}
# list_demo.append(dict_country)
# for item in list_demo:
#     print(item)
#
# for key, value in dict_country.items():
#     print("%s 的景区有:%s, 美食有:%s"%(key, value[0], value[1]))