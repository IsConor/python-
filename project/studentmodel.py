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