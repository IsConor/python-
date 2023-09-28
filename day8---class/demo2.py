
'''

    面向对象：考虑问题从对象的角度出发
    抽象：从多个事物中，舍弃个别的/非本质的特征，抽出共性的本质过程
    三大特征：
        封装：将每个变化点单独分解到不同的类中，例如老张开车去东北：定义人类、车类
        继承：重用现有类的功能和概念，并在此基础上进行扩展。例如：图形管理器，统计圆形/矩形。。。面积
        多态：调用基类那个比较抽象的方法，执行派生类具体的方法，派生类重写基类的抽象方法
    设计原则
        开闭原则：允许增加新功能，不允许修改客户端代码
        单一职责：一个类有且只有一个改变的原因。
        依赖倒置：调用抽象（父），不要调用具体（子），抽象不要依赖于具体。
        组合复用：如果仅仅是代码的复用，优先使用组合。
'''


# 定义员工管理器，1，管理所有员工，2.计算所有员工工资，
# 员工：程序员：底薪+项目分红   销售：底薪+销售额*0.05   软件测试。。。。

class PersonnelManager:
    """
        员工管理器：负责增加、删除、查询员工薪资，查看员工信息
    """
    def __init__(self):
        self.__manager = []
    def add_personnel(self, personnel):
        if isinstance(personnel,Personnel):
            self.__manager.append(personnel)
        else:
            raise ValueError()
    def del_personnel(self, name):
        for item in self.__manager:
            if item.name == name:
                self.__manager.remove(item)
    def count_personnel_money(self, personnel):
        return personnel.count_money()
    def show_personnel_info(self, personnel):
        if personnel in self.__manager:
            personnel.show_info()
        else:
            print("this personnel is not in manager")

class Personnel:
    """
        基类（抽象类）
    """
    def show_info(self):
        """
            查看自己的信息
        """
        pass
    def count_money(self):
        """
            计算薪资
        :return: 总薪资
        """
        pass
class Programer(Personnel):
    """
        程序员类
    """
    def __init__(self,name, age, base_money, red_money):
        self.name = name
        self.age = age
        self.base_money = base_money
        self.red_money = red_money
    def show_info(self):
        print("program personnel name:%s, age:%d"%(self.name, self.age))
    def count_money(self):
        """
            薪资= 底薪 + 项目分红
        :return: 总薪资
        """
        return self.base_money + self.red_money
class Market(Personnel):
    """
        销售类
    """
    def __init__(self,name, age, base_money, up_money):
        self.name = name
        self.age = age
        self.base_money = base_money
        self.up_money = up_money
    def show_info(self):
        print("market personnel  name:%s, age:%d" % (self.name, self.age))
    def count_money(self):
        """
            薪资 = 底薪 + 提成
        :return:
        """
        return self.base_money + self.up_money

pm = PersonnelManager()
program = Programer("aaa", 18, 1800, 2000)
market = Market("bbb",81, 1500, 1000)

pm.add_personnel(program) #添加员工
pm.add_personnel(market)
print("销售的薪资: ",pm.count_personnel_money(market)) # 计算薪资
print("程序员的薪资: ", pm.count_personnel_money(program))
pm.del_personnel("bbb") #删除姓名为bbb的员工
pm.show_personnel_info(market) #输出员工信息（姓名、年龄）
pm.show_personnel_info(program)



# class GraphicManager:
#     """
#         图形管理器
#     """
#     def __init__(self):
#         self.__graphics = []
#     def add_graphics(self,graphics):
#         if isinstance(graphics,Graphics):
#             self.__graphics.append(graphics)
#         else:
#             raise ValueError()
#     def get_total_area(self):
#         total_area = 0
#         # 遍历图形列表，累加每个图形的面颊
#         for item in self.__graphics:
#             total_area += item.caculate_area()
#         return total_area
#
# class Graphics:
#     """
#         图形类
#     """
#     def caculate_area(self):
#         pass
# class Rect(Graphics):
#     """
#         矩形
#     """
#     def __init__(self, lenth, width):
#         self.lenth = lenth
#         self.width = width
#     def caculate_area(self):
#         return self.lenth * self.width
# class Circular(Graphics):
#     """
#         圆形
#     """
#     def __init__(self,r):
#         self.r = r
#
#     def caculate_area(self):
#         return self.r**2 * 3.14
#
# c01 = Circular(2)
# cir = GraphicManager()
# cir.add_graphics(c01)
# print(cir.get_total_area())



# class Vehicle:
#     def transport(self, str_position):
#         pass
#
# class Person:
#     def __init__(self,name):
#         self.name = name
#     def go_to(self,vehicle, str_position):
#         vehicle.transport(str_position)
#
# class Car(Vehicle):
#     def transport(self, str_position):
#         print("car is drived ",str_position)
# class Airplane(Vehicle):
#     def transport(self, str_position):
#         print("Airplane is fly to ",str_position)
#
# p1 = Person("lz")
# c1 = Car()
# a1 = Airplane()
# p1.go_to(a1,"东北")
# p1.go_to(c1, "东北")



# class Car:
#     def __init__(self,color,logo):
#         self.color = color
#         self.logo = logo
#
# class Smallcar(Car):
#     def __init__(self, pw, color, logo):
#         super().__init__(color,logo) #调用父类构造函数
#         self.pw = pw
#
# c1 = Car("red","aodi")
# s1 = Smallcar(100,"red","aodi")
# print(isinstance(s1, Smallcar))




# class Person:
#     def __init__(self,name):
#         self.name = name
#
# class Student(Person):
#     # 子类若没有构造函数，使用父类的
#     def __init__(self,name, score):
#         super().__init__(name)
#         self.score = score
#
# s01 = Student("张三",100)
# print(s01.score)


# class Person:
#     def say(self):
#         print("Person say")
#
# class Teacher(Person):
#     def teach(self):
#         pass
#
# T01 = Teacher
# print(isinstance(T01,Person))
# print(issubclass(Teacher,Person))


# class Student:
#     __slots__ = ("name")
#     def __init__(self,name):
#         self.name = name
#
# s1 = Student("aaa")
# s1.name = "bbb"
# s1.nema = "aaa"
# print(s1.name)
# print(s1.nema)