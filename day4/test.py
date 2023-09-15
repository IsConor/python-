'''
    类的练习
'''

class Person(object):
    def __init__(self, NAME, AGE):
        self.name = NAME
        self.age = AGE

    def setName(self, arg1):
        self.name = arg1
    def getName(self):
        return self.name

person = Person("bao", 18)
person.setName("haha")
print(person.getName())
