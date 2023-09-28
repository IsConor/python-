'''
    技能系统
    三大特征：
        封装：将每种影响效果单独做成类
        继承：将各种影响效果抽象为SkillImpactEffect类，隔离技能释放器与各种影响效果的变化
        多态：技能释放器通过调用抽象类来调用各种影响效果、 各种影响效果通过重写抽象类中的方法impact实现多态
    六大原则：
        开闭原则：增加新（技能/影响效果），不修改释放器
        单一职责：SkillImpactEffect 负责隔离变化，DamageEffect负责定义具体效果，SkillDeployer负责释放技能
        依赖倒置：释放器没有调用具体的影响效果，
'''

class SkillImpactEffect:
    """
        技能影响效果
    """
    def impact(self):
        raise NotImplementedError()

class DamageEffect(SkillImpactEffect):
    """
        伤害生命效果
    """
    def __init__(self, value):
        self.value = value
    def impact(self):
        print("扣你%dhp" % (self.value))
class LowerDeffenseEffect(SkillImpactEffect):
    """
        降低防御力
    """
    def __init__(self, value, time):
        self.value = value
        self.time = time
    def impact(self):
        print("降低%d防御力,持续%d秒" % (self.value, self.time))

class DizzinessEffect(SkillImpactEffect):
    def __init__(self, time):
        self.time = time
    def impact(self):
        print("眩晕%d秒" % (self.time))

class SkillDeployer:
    """
        技能释放器
    """
    def __init__(self, name):
        self.name = name
        # 加载配置文件 {技能名称:[效果1，效果2...]，....}
        self.__dict_skill_config = self.__load_config_file()
        # 创建效果对象
        self.__effect_object = self.__create_effect_objects()

    def __load_config_file(self):
        # 加载文件
        return {
            "xlsbz":["DamageEffect(200)", "LowerDeffenseEffect(-10,5)", "DizzinessEffect(6)"],
            "lmsj":["DamageEffect(200)", "DizzinessEffect(6)"]
        }
    def __create_effect_objects(self):
        # 根据name创建相应的技能对象
        list_effect_name = self.__dict_skill_config[self.name]
        list_effect_object = []
        for item in list_effect_name:
            list_effect_object.append(eval(item))
        return list_effect_object
    # 生成技能（执行效果）
    def generate_skill(self):
        print("%s 技能释放了" % (self.name))
        for item in self.__effect_object:
            item.impact()

xlsbz = SkillDeployer("xlsbz")
xlsbz.generate_skill()