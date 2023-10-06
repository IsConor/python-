from studentmanagercontroller import StudentManagerController
from studentmodel import StudentModel
class StudentManagerView:
    """
        视图
    """
    def __init__(self):
        self.__manager = StudentManagerController()
    def __display_menu(self):
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")

    def __select_menu(self):
        item = input("请输入: ")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__show_student()
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__update_student()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()
    def __input_student(self):
        """
            输入学生信息，将学生信息构建学生模型加入管理控制器调度
        :return:
        """
        name = input("please input student name>")
        age = int(input("please input student age>"))
        score = int(input("please input student score>"))
        stu = StudentModel(name,age,score)
        self.__manager.add_student(stu)

    def __show_student(self):
        """
            遍历所有管理控制器中的学生信息
        :return:
        """
        self.__manager.show_student()
    def __delete_student(self):
        """
            删除姓名为name的学生信息
        :param name:
        :return:
        """
        name = input("please input student name if you want delete>")
        self.__manager.del_student(name)

    def __update_student(self):
        """
            将指定ID的学生信息进行更改
        :return:
        """
        id = int(input("please input you want update student's id>"))
        name = input("please input you want update student's name>")
        age = int(input("please input student age>"))
        score = int(input("please input student score>"))
        stu = StudentModel(name, age, score,id)
        self.__manager.update_student(stu)