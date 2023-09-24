'''
    元组: 由一系列变量组成的不可变序列容器，一旦创建，不可以再添加/删除/修改元素
        作用，不变的数据用元组储存相比与列表更节省内存，变量交换的原理就是创建元组 x, y = y, x
        列表扩容原理：1.列表都会预留空间，当空间不足时，会再创建新列表，将原有数据拷贝到新列表中，替换引用
                元组是按需分配，不会预留空间
        基础操作：
    字典 dict
        定义：由一系列键值对组成的可变映射容器，键必须唯一且不可变（字符串/数字/元组），值没有限制
        优点：根据键获取值，读取速度快，代码可读性相对于列表来说更高
        缺点：内存占用相对大，获取值只能根据键，不灵活
'''

# 在控制台中获取多个人的多个喜好，例如：
#请输入姓名：
#请输入第一个喜好：
#请输入第二个喜好：
#..... 输入空字符停止，最后在控制台打印所有人的所有喜好
# list_demo = []
# dict_person = dict() # 字典 {name, [喜好]}
# list_like = []
# while True:
#     name = input("please input person name:")
#     if name == "":
#         break
#     ret = 0
#     while True:
#         ret += 1
#         like = input("please input %s's %dlike:"%(name, ret))
#         if like == "":
#             break
#         list_like.append(like)
#     dict_person[name] = list_like
#     list_demo.append(dict_person)
# for name, likes in dict_person.items():
#     #key 的 like have value[:]
#     print("%s's like have %s"%(name, str(likes[:])))
# for item in list_demo:
#     print(item)




#[{name:name}, {age:age}, {number:number}, {sex:sex}]


# 录入姓名、年龄、成绩、性别，如果录入空，则结束并打印所有学生信息
# 列表内嵌字典
# list_student_info = []
# while True:
#     name = input("please input name >")
#     if name == "":
#         break
#     age = int(input("please input age >"))
#     number = int(input("please input number >"))
#     sex = input("please input sex >")
#     dict_student = {"name":name, "age":age, "number":number, "sex":sex}
#     list_student_info.append(dict_student)
# for item in list_student_info:
#     print("%s age = %d, num = %d, sex = %s"%(item["name"], item["age"], item["number"], item["sex"]))


#字典内嵌字典
# dict_student_info = dict()
# while True:
#     name = input("please input name >")
#     if name == "":
#         break
#     elif name in dict_student_info:
#         print("error, student %s is already"%name)
#     age = int(input("please input age >"))
#     number = int(input("please input number >"))
#     sex = input("please input sex >")
#     dict_student_info[name] = {"age":age, "number":number, "sex":sex}
#
# for key, value in dict_student_info.items():
#     print("name=%s, age=%d, num=%d, sex=%s" %(key, value["age"], value["number"], value["sex"]))



# 字典内嵌元组/列表
# dict_student_info = dict()
# while True:
#     name = input("please input name >")
#     if name == "":
#         break
#     elif name in dict_student_info:
#         print("error, student %s is already"%name)
#     age = int(input("please input age >"))
#     number = int(input("please input number >"))
#     sex = input("please input sex >")
#
#     tuple01 = (age, number, sex)
#     dict_student_info[name] = tuple01
# for key, value in dict_student_info.items():
#     print("name:%s, age:%d, number:%d, sex:%s"%(key, value[0], value[1], value[2]))



# # 在控制台中循环录入商品信息，名称和单价，如果输入空字符，则停止录入，逐行打印所有信息
#
# dict01 = dict()
# while True:
#     name = input("please input name >")
#     if name == "":
#         break
#     if name in dict01:
#         print("已存在，请勿重复操作")
#         continue
#     number = input("please input number >")
#     dict01[name] = number
#
# for k, v in dict01.items():
#     print("name:%s : number: %s" %(k, v))













# # 1 创建
# # 空
# dict01 = {}
# # 默认值
# dict02 = {"wj":100, "zm":80, "zr":90}
# #dict02 = dict([("a", "b"), ("c", "d")])
# print(dict02)
# # 2 添加 -- (之前不存在key）
# dict02["e"] = 60
#
# # 3 查找元素 -- （如果key不存在，查找时会报错），所以查找时要加判断
# if "wj" in dict02:
#     print(dict02["wj"])
#
# # 4 修改元素 -- （之前存在key）
# dict02["wj"] = "1"
# print(dict02)
#
# # 5 删除元素
# del dict02["e"]
# print(dict02)
#
# # 6 遍历字典 -- 得到的时key
# # 获取键
# for key in dict02:
#     print(key)
# # 获取值
# for item in dict02:
#     print(dict02[item])
# for item in dict02.values():
#     print(item)
# # 获取键和值
# # for item in dict02.items():
# #     print(item)
#
# for k, v in dict02.items():
#     print(k)
#     print(v)



# # 在控制台中录入日期（年月），计算这是这一年的第几天，例：3月5日  ->  1月天数+2月天数+5
# tuple_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
#
# month = int(input("please input month>"))
# day = int(input("please input day>"))
# # date = 1
# # for item in range(month-1):
# #     date += tuple_month[item]
# # print(date + day)
#
# to_day = sum(tuple_month[:month-1])
# to_day+=day
# print(to_day)


#
# list_month = [item for item in range(1, 13)]
# tuple_month = tuple(list_month)
# i = input("please input month>")
# if i in tuple_month:
#     print("30天")
# elif i == 2:
#     print("28天")
# else:
#     print("31天")



# # 1 创建元组
# # 空
# tuple01 = ()
# tuple01 = (["a", "b"])
# list01 = list(tuple01)
# print(tuple01)
#
# # 具有默认值
# tuple02 = (1, 2, 3)
# print(tuple02)
#
# # 元组只有一个元素时，后面要加逗号
# tuple03 = (100,)
# print(type(tuple03))
#
# #  不能增加
#
#
#
# # 2 获取元素 --- 索引  切片
# tuple04 = ("a", "b", "c", "d")
# print(type(tuple04[1]))
# print(tuple04[:])
# a,b,c,d = tuple04
# print(a)
#
# # 3 遍历元素
# # 正向
# for item in tuple04:
#     print(item)
# # 反向
# for item in range(len(tuple04)-1, -1, -1):
#         print(tuple04[item])