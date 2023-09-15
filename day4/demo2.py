'''
    面向对象编程：
        类
            类名：驼峰命名法：PrintStar Printstar
            属性：
            方法：
        对象
    面向过程编程：顺序
'''

# 创建一个类  --- 其中self相当于this指针
class Make_Plane(object):
    #构造函数 --- 在构造函数中声明并初始化成员变量
    def __init__(self, COLOR, WHEELNUM):
        self.color = COLOR
        self.wheelNum = WHEELNUM
    # 成员函数
    def move(self):
        print("fly")
    def getPlaneInfo(self):
        print("轮胎数量%d, 飞机颜色%s" %(self.wheelNum,self.color))

#实例化对象
myPlane = Make_Plane("yellow", 4)
myPlane.move()
print(myPlane.color)
myPlane.color = "blue"
myPlane.getPlaneInfo()

yourPlan = Make_Plane("red", 10)
yourPlan.color = "red"
yourPlan.getPlaneInfo()
