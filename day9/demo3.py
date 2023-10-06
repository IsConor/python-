"""
    包package：
    作用：让一些相关的数据、函数、类的文件有逻辑的组织在一起
    python程序结构：
    文件夹 ---- 项目根目录
        包
            模块
                类
                    函数
                        语句
"""
# from package01.package02.moduleb import *
# from package01.modulea import *
# fun01()
# from package01.package02.moduleb import *
# fun01()

# from package01.modulea import *
# fun01()
#
# from package01.package02.moduleb import *
# fun01()

class AgeError(Exception):
    def __init__(self, message, line, err_number):
        self.message = message
        self.line = line
        self.err_number = err_number

class Wife:
    def __init__(self,age):
        self.age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if 0 <= value <= 31:
            self.__age = value
        else:
            raise AgeError("out of range", 38,1001)
try:
    w01 = Wife(91)
except AgeError as e:
    print(e.message,e.line,e.err_number)