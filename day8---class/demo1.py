'''
    封装数据
        优势：更符合人类的思维方式，将数据与对数据的操作封装到一起
        使用property封装变量
    封装行为
        优势：以”模块化“的方式进行编程（可以集中精力设计/组织/指挥多个类协同工作）
    静态方法引入：
        总结：
            实例方法：操作对象的变量
            类方法：操作类的变量
            静态方法：既不需要操作实例变量，也不需要操作类变量
    类变量: 被所有对象共享
'''

# class Person:
#     def __init__(self, name):
#         self.name = name
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,value):
#         self.__name = value
#     def go_to(self, destination, type):
#         print(self.name,"去",destination)
#         type.run(destination)
# class Transport:
#     def run(self, destination):
#         print("行驶到:",destination)
#
# Lz = Person("老张")
# car = Transport()
# Lz.go_to("东北",car)



# 定义敌人类，姓名，攻击力，血量，

# class Empty:
#     def __init__(self,name,atk,hp):
#         self.name = name
#         self.__atk = atk
#         self.__hp = hp
#
#     @property  #创建property对象，只负责拦截读取操作
#     def atk(self):
#         return self.__atk
#     @atk.setter  #只负责拦截写入操作
#     def atk(self,value):
#         if 10 <= value <= 50:
#             self.__atk = value
#         else:
#             raise ValueError("超出范围")
#     @property
#     def hp(self):
#         return self.__hp
#     @hp.setter
#     def hp(self,value):
#         if 0 <= value <= 100:
#             self.__hp = value
#         else:
#             raise ValueError("超出范围")
#
#     def print_self_info(self):
#         print(self.name, self.atk, self.hp)
#
# empty = Empty("aaa",12, 99)
# empty.print_self_info()
#
#
# print(empty.atk)



# class Wife:
#     def __init__(self,name,age,weight):
#         self.name = name
#         # 本质：障眼法
#         # 实际将变量 age 改为 _类名__age
#         self.set_age(age)
#         self.set_weight(weight)
#
#     def get_age(self):
#         return self.__age
#     def set_age(self,age):
#         self.__age = age
#     def get_weight(self):
#         return self.__weight
#     def set_weight(self,wei):
#         self.__weight = wei

# w01 = Wife("aaa", 87, 87)
# w01.name = "bbb"
# print(w01.name)
# #w01._Wife__age = 1 # 修改了类中定义的私有变量, 在python中不要试图寻找带有__的变量（私有）
#
# #print(w01.__dict__) #python内置变量，存储对象的实例变量的字典
# w01.set_age(18)
# print(w01.get_age())
#


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





