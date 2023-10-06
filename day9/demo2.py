# 将学生管理系统分为4个模块 /project/main.py studentmanager.py studentmodel.py studentview.py

# from module01 import MyClass02
# 主模块叫做：__main__
# 非主模块叫做：真名
# print(__name__)

# ---------------------------------------------- 时间处理模块 -------------------------------------------------

# import time
#
# # 1获取当前时间戳（从1970年1月1日到现在经过的秒数）
# print(time.time())
#
# # 2时间元组(年、月、日、时、分、秒、星期、夏令时)
# print(time.localtime(1696563646))
# tuple_time = time.localtime()
# # 元组的操作来获取时间
# for item in tuple_time:
#     print(item)
#
# # 类的操作获取时间
# print(time.localtime().tm_year)
#
# # 时间元组 -> 时间戳
# print(time.mktime(tuple_time))
#
# # 时间元组 --> str
# str_time = time.strftime("%y-%m-%d: %H:%M:%S",tuple_time)
# print(str_time)
#
# # str --> 时间元组
# tuple_time1 = time.strptime(str_time,"%y-%m-%d: %H:%M:%S")
# print(tuple_time1)

# -------------------------------------------- 根据年月日 获取星期数 -----------------------------------------------------
# import time
# def get_week(year, month, day):
#     tuple_time = time.strptime("%d-%d-%d"%(year, month, day), "%Y-%m-%d")
#     dict_week = {
#         0:"星期一",
#         1:"星期二",
#         2:"星期三",
#         3:"星期四",
#         4:"星期五",
#         5:"星期六",
#         6:"星期日"
#     }
#     return dict_week[tuple_time.tm_wday]
#
#
# print(get_week(2023,10,6))

# --------------------------------------------- 根据生日 计算活了多少天-------------------------------------------------------------
# import time
# def life(year, month, day):
#     tuple_time = time.strptime("%d-%d-%d"%(year,month,day), "%Y-%m-%d")
#     life_second = time.time() - time.mktime(tuple_time)
#     return int(life_second / 3600 // 24)
# print(life(1998,5,13))