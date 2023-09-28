'''
    少林
        技能1     特效
        技能2     特效
        技能3     特效
    逍遥
        技能1     特效
        技能2     特效
        技能3     特效
    丐帮
        技能1     特效
        技能2     特效
        技能3     特效
'''

class School:
    def attack(self, school):
        pass
class Shaolin(School):
    def __init__(self, hp, fp):
        self.__hp = hp
        self.fp = fp
    def shaolinpugong(self, xiaoyao):
        print("造成每秒10外伤攻击伤害")
        xiaoyao.hp -= 10
    def attack(self, xiaoyao):
        str01 = input("选择技能>")
        if str01 == "1":
            self.shaolinpugong(xiaoyao)

class Xiaoyao(School):
    def __init__(self, hp, fp):
        self.__hp = hp
        self.fp = fp
    def xiaoyaopugong(self, shaolin):
        print("造成每秒30外伤攻击伤害")
        shaolin.hp -= 30

    def attack(self, shaolin):
        str01 = input("选择技能>")
        if str01 == "1":
            self.xiaoyaopugong(shaolin)

school = School()
shaolin = Shaolin(100,100)
xiaoyao = Xiaoyao(100,100)
shaolin.attack(xiaoyao)
xiaoyao.attack(shaolin)