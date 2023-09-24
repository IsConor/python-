'''
    封装数据
    静态方法引入：
        总结：
            实例方法：操作对象的变量
            类方法：操作类的变量
            静态方法：既不需要操作实例变量，也不需要操作类变量
    类变量: 被所有对象共享
'''







# # 静态方法引入
# list01 = [
#     ["00","01","02","03"],
#     ["10","11","12","13"],
#     ["20","21","22","23"]
# ]
#
# class Vector2:
#     '''
#         二维向量
#         可以表示位置，也可以表示方向
#     '''
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     @staticmethod
#     def left():
#         # 静态方法：表示左边方向
#         return Vector2(0,-1)
#     @staticmethod
#     def right():
#         # 静态方法：表示右边方向
#         return Vector2(0,1)
#
#
# # 作用：位置 + 方向
# pos01 = Vector2(1,2)
# l01 = pos01.left()
# pos01.x += l01.x
# pos01.y += l01.y
# print(pos01.x, pos01.y)
#
#
# # 在二维列表中，获取指定位置，指定方向，指定数量的元素
# class DoublelistHelper:
#     @staticmethod
#     def get_elements(target, vect_pos, vect_dir, count):
#         list_result = []
#         for i in range(count):
#             vect_pos.x += vect_dir.x
#             vect_pos.y += vect_dir.y
#             element = target[vect_pos.x][vect_pos.y]
#             list_result.append(element)
#         return list_result
#
# re = DoublelistHelper.get_elements(list01,Vector2(1,0), Vector2.right(),3)
# print(re)


# 类变量
# class ICBC:
#     total_money = 1000000
#     # 类方法没有对象地址self，不能访问实例成员
#     @classmethod
#     def print_money(cls):
#         print(cls.total_money)
#     def __init__(self,name,money):
#         self.name = name
#         self.money = money
#         ICBC.total_money -= money
#
#
# i01 = ICBC("guangqumenzhihang", 100000)
# i02 = ICBC("taoyantingzhihang", 100000)
#
# # 通过类名访问类方法会自动将类名传入类方法
# ICBC.print_money()





