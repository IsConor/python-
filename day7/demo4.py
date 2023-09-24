'''
    面向对象 --- 类
'''

class Student(object):
    def __init__(self,NAME,AGE,SCORE,SEX):
        self.name = NAME
        self.age = AGE
        self.score = SCORE
        self.sex = SEX

    def print_self_info(self):
        print("name=%s,age=%d,score=%d,sex=%s"%(self.name, self.age, self.score,self.sex))


# 在列表list01中寻找name为ccc的成员，并打印成员信息

list01 = [
    Student("aaa", 28, 100, "women"),
    Student("bbb",68,62, "men"),
    Student("ccc", 30, 95, "men"),
    Student("ddd", 29, 70, "men"),
    Student("eee", 18, 90, "women")
]

def find_name(name):
    '''
        在列表中根据姓名找到对应的成员对象
    :param name: 要查找的姓名
    :return: 找到的对象
    '''
    for stu in list01:
        if stu.name == name:
            return stu

def find_if_women():
    '''
        查找所有性别为women的成员
    :return: 存放所有性别为women的成员对象的列表
    '''
    list_tmp = [item for item in list01 if item.sex=="women"]
    return list_tmp

def find_num_of_age(num):
    '''
        统计所有成员中年龄大于num的成员数量
    :param num: 年龄
    :return: 计算以后的数量
    '''
    count = 0
    for item in list01:
        if item.age >= num:
            count += 1
    return count

def zero_student_score():
    '''
        将列表中的所有学生成绩归零
    :return:
    '''
    for item in list01:
        item.score = 0

def get_name_for_list():
    '''
        获取列表中所有成员的姓名
    :return: 存放所有成员姓名的列表
    '''
    list_tmp = [item.name for item in list01]
    return list_tmp

def find_best_age():
    '''
        在对象列表中寻找age最大的对象
    :return: age最大的对象
    '''
    max_age = list01[0]
    for item in range(1,len(list01)):
        if list01[item].age > max_age.age:
            max_age = list01[item]
    return max_age




# 从控制台输入信息，存储在列表中，实现遍历
#
# list_student = []
# while True:
#     name = input("please input name>")
#     if name == "":
#         break
#     age = int(input("please input age >"))
#     score = int(input("please input score >"))
#     sex = input("please input sex >")
#     stu = Student(name,age,score,sex)
#     list_student.append(stu)
#
# for stu in list_student:
#     stu.print_self_info()
























