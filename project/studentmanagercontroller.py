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