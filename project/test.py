'''
    测试
'''
list01 = []
list_demo = {"id":1,"name":44, "age":3, "score":4}
list_demo1 = {"id":1,"name":2, "age":3, "score":4}
list01.append(list_demo1)
list01.append(list_demo)
for item in list01:
    if item["name"] == 44:
        list01.remove(item)

for item in list01:
    print(item)

# class Person:
#     def __init__(self, name, gongfu, money):
#         self.name = name
#         self.gongfu = gongfu
#         self.money = money
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,value):
#         self.__name = value
#     @property
#     def gongfu(self, value):
#         return self.__gongfu
#     @gongfu.setter
#     def gongfu(self, value):
#         self.__gongfu = value
#     @property
#     def money(self):
#         return self.__money
#     @money.setter
#     def money(self, value):
#         self.__money = value
#
#     def work(self, value):
#         self.money += value
#         print(self.name,"上班挣了",value)
#
#
# wuji = Person("无忌","九阳", 100)
# zhaomin = Person("赵敏", "化妆", 100)
#
# wuji.work(5000)
# print(wuji.money)





'''
    面向对象
'''

# class Person:
#     def __init__(self,name,money):
#         self.name = name
#         self.money = money
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,value):
#         self.__name = value
#     @property
#     def money(self):
#         return self.__money
#     @money.setter
#     def money(self,value):
#         self.__money = value
#
#     def goto(self, bank, behave,des):
#         print(self.name,"go to", bank.name,behave.behave(des))
#
# class Bank:
#     money = 100000
#     def __init__(self,name):
#         self.name = name
#
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,value):
#         self.__name = value
#     def get_money(self, person, money):
#         if Bank.money > money:
#             Bank.money -= money
#             person.money += money
#         else:
#             raise ValueError("银行钱不够")
#
# xm = Person("小明",100)
# yh = Bank("招商")
# yh.get_money(xm,10000)
# print(xm.money)
# print(Bank.money)





'''
    定义敌人类
        ---数据：姓名，血量，基础攻击力，防御力
        ---行为：打印个人信息
'''
#
# class Enemy:
#     def __init__(self,name,hp,atk,defense):
#         self.name = name
#         self.hp = hp
#         self.atk = atk
#         self.defense = defense
#
#     def print_self_info(self):
#         print(self.name,self.hp,self.atk,self.defense)
#
#
# list01 = [
#     Enemy("xmel", 0, 120, 1),
#     Enemy("ck",60,100,40),
#     Enemy("xx",120,130,60),
#     Enemy("mb",5000,1309, 690)
# ]
#
# def find01(name):
#     '''
#         寻找姓名为name的对象
#     :param name: 要查找的姓名
#     :return: 找到的对象
#     '''
#     for item in list01:
#         if item.name == name:
#             return item
#
# e01 = find01("mb")
# # 如果没找到，返回None
# # 先判断是否为None，再调用
# if e01:
#     e01.print_self_info()
# else:
#     print("not find")
#
# def find02():
#     '''
#         找到死掉的对象
#     :return: 列表
#     '''
#     list_result = []
#     for item in list01:
#         if item.hp == 0:
#             list_result.append(item)
#     return list_result
#
# re = find02()
# for item in re:
#     item.print_self_info()
#
# def calculate01():
#     '''
#         计算平均攻击力
#     :return: 计算以后的结果
#     '''
#     sum_atk = 0
#     for item in list01:
#         sum_atk += item.atk
#     return sum_atk / len(list01)
#
# print(calculate01())
#
# def delete01():
#     '''
#     删除防御力小于10的对象
#     :return: none
#     '''
#     for item in range(-1,-len(list01)-1, -1):
#         if list01[item].defense < 10:
#             del list01[item]
#
#
# delete01()
# for item in list01:
#     item.print_self_info()


'''静态成员方法'''
# # 在二维列表中获取22位置向上两个元素
#
# class Vector:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     @staticmethod
#     def up():
#         return Vector(-1,0)
#     @staticmethod
#     def down():
#         return Vector(1,0)
#     @staticmethod
#     def left():
#         return Vector(0,-1)
#     @staticmethod
#     def right():
#         return Vector(0,1)
#
#
# class ListHelper:
#     @staticmethod
#     def get_elements(target, vect_pos, vect_dir, count):
#         list_result = []
#         for item in range(count):
#             vect_pos.x += vect_dir.x
#             vect_pos.y += vect_dir.y
#             element = target[vect_pos.x][vect_pos.y]
#             list_result.append(element)
#         return list_result
#
# list01 = [
#     ["00","01","02","03"],
#     ["10","11","12","13"],
#     ["20","21","22","23"]
# ]
#
# re = ListHelper.get_elements(list01, Vector(2,2), Vector.up(), 2)
# print(re)


'''类对象测试'''

# class Wife:
#     count = 0
#     @classmethod
#     def print_count(cls):
#         print(cls.count)
#     def __init__(self,name, sex):
#         self.name = name
#         self.sex = sex
#         Wife.count += 1
#
#     def print_wife(self):
#         print("name=%s, sex=%s"%(self.name, self.sex))
#
# w1 = Wife("aaa","women")
# w2 = Wife("bbb", "men")
#
# w1.print_wife()
# w2.print_wife()
# Wife.print_count()
