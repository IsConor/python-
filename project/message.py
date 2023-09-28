'''
    信息管理系统
'''

class StudentModel:
    """
        学生模型
    """
    def __init__(self,NAME="",AGE=0,SCORE=0,ID=0):
        """
            创建学生对象
        :param NAME: 姓名
        :param AGE: 年龄
        :param SCORE: 成绩
        """
        self.name = NAME
        self.age = AGE
        self.score = SCORE
        self.id = ID
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value_age): # 年龄取值范围0~35
        if 0 < value_age < 35:
            self.__age = value_age
        else:
            raise ValueError("out of range")
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score_value): # 给成绩赋值 取值范围0~100
        if 0 <= score_value <= 100:
            self.__score = score_value
        else:
            raise ValueError("out of range")
class StudentManagerController:
    """
        学生管理控制器，负责业务逻辑处理
    """
    init_id = 0 # 类变量，标识初始编号
    def __init__(self):
        self.__stu_list = []
    @property
    def stu_list(self):
        """
            学生列表
        :return: 返回对象列表
        """
        return self.__stu_list
    def add_student(self,student):
        """
            添加一个新的学生
        :param student: 没有编号的学生信息
        :return:
        """
        StudentManagerController.init_id+=1
        student.id += StudentManagerController.init_id
        dict_demo = {"id":student.id,"name":student.name, "age":student.age, "score":student.score}
        self.stu_list.append(dict_demo)
    def del_student(self,name):
        """
            删除一个学生
        :param name: 要删除的学生姓名
        :return:
        """
        for item in self.stu_list:
            if item["name"] == name:
                self.stu_list.remove(item)
                return True
        return False
    def show_student(self):
        """
            遍历学生列表，打印学生的所有信息
        :return:
        """
        for item in self.stu_list:
            print("ID:%d 姓名:%s 年龄:%d 成绩:%d"%(item["id"], item["name"],item["age"], item["score"]))

    def update_student(self, stu_info):
        """
            根据编号修改信息
        :return:
        """
        for item in self.stu_list:
            if item["id"] == stu_info.id:
                item["name"] = stu_info.name
                item["age"] = stu_info.age
                item["score"] = stu_info.score


'''测试

s01 = StudentModel("aaa",18,100) # 定义学生模型
s02 = StudentModel("bbb",19,90)
manager = StudentManagerController() # 业务控制器实例对象manager
manager.add_student(s02)   # 添加学生
manager.add_student(s01)
print(manager.del_student("aaa")) # 删除姓名为aaa的学生 ，return为True则删除成功
manager.update_student(StudentModel("lll", 20, 80,1)) # 根据id更改信息
manager.show_student() # 遍历所有学生信息
'''

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




view = StudentManagerView()
view.main()