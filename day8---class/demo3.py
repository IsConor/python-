'''
    内置可重写函数：在python中，以双下划线开头以双下划线结尾的是系统定义的成员，我们可以进行重写，从而改变其行为
        __str__函数：将对象转换为字符串（对人友好的）
        __repr__函数：将对象转换为字符串（解释器可识别的）
            repr函数返回python格式的字符串
            eval函数根据字符串执行代码
    运算符重载：__add__  __sub__ __mul__
    多继承：同名方法解析顺序： 类.mro() -> 返回的是多继承中寻找方法的顺序
    技能系统
'''








# class StudentModel:
#     def __init__(self, name="", age=0, score=0):
#         self.name = name
#         self.age = age
#         self.score = score
#     def __str__(self):
#         """
#             将对象变成字符串
#         :return:
#         """
#         return "my name is %s, age is %d, score is %d"%(self.name, self.age, self.score)
#     def __repr__(self):
#         """
#             解释器可识别，有格式
#         :return:
#         """
#         return "StudentModel('%s',%d,%d)" % (self.name, self.age, self.score)
#
# s01 = StudentModel("aaa",27,100)
# str01 = str(s01)
# print(s01)
# print(str01)
#
# s02 = eval(repr(s01))
#
# print(s02)

# ------------------------------------------ 练习 -------------------------------------------------------------

# 创建Enemy类对象，将对象打印在控制台中，格式自定
# 克隆Enemy类对象，体会克隆对象的改变不影响原对象
# class Enemy:
#     def __init__(self,name,age,hp):
#         self.name = name
#         self.age = age
#         self.hp = hp
#     def __str__(self):
#         return "name=%s,age=%d,hp=%d" % (self.name, self.age, self.hp)
#     def __repr__(self):
#         return "Enemy('%s',%d,%d)" % (self.name, self.age, self.hp)
#
# e01 = Enemy("aa",18,100)
# print(e01)
#
# e02 = eval(repr(e01))
# e02.age = 20
# e02.name = "bb"
# print(e02)
# ------------------------------------------ 运算符重载 -------------------------------------------------------------

# class Vector1:
#     def __init__(self, x):
#         self.x = x
#     def __str__(self):
#         return "一维向量的分量是:" + str(self.x)
#     def __add__(self, other):
#         return Vector1(self.x + other)
#
# v01 = Vector1(10)
# print(v01 + 2)

# ---------------------------------------------- test -------------------------------------------------------------

# class Vector1:
#     def __init__(self,x):
#         self.x = x
#     def __str__(self):
#         return "一维向量的分量是:" + str(self.x)
#     def __sub__(self, other):
#         return Vector1(self.x - other)
#     def __mul__(self, other):
#         return Vector1(self.x * other)
#
# v1 = Vector1(10)
# print(v1 * 10)
# print(v1 - 5)

# ------------------------------------------- 反向算数运算符重载 r test---------------------------------------------------
# 实现数值与自定义类的对象的减法，乘法运算
# class Vector:
#     def __init__(self,x):
#         self.x = x
#     def __str__(self):
#         return "一维向量的分量:" + str(self.x)
#
#     def __radd__(self, other):
#         return Vector(other + self.x)
#     def __rsub__(self, other):
#         return Vector(other - self.x)
#     def __rmul__(self, other):
#         return Vector(other * self.x)
# v1 = Vector(10)
# print(100 - v1)
# print(2 * v1)

# ----------------------------------------------------------------------------------------------------------------------

#
# class Vector:
#     def __init__(self, x):
#         self.x = x
#     def __str__(self):
#         return str(self.x)
#     def __iadd__(self, other):
#         self.x += other
#         return self
#
# v1 = Vector(10)
# v1 += 2
# print(v1,id(v1))

