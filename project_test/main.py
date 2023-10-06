# from skill_system.skill_deployer import func
# func()
#
# def main_func():
#     print("I am main")
#
# from skill_system import *
# skill_manager.func()
# skill_deployer.func()
#
# import sys
# print(sys.path)
class Wife:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 0 <= value <= 31:
            self.__age = value
        else:
            raise ValueError("No")

try:
    w01 = Wife(81)
except:
    print("please again")