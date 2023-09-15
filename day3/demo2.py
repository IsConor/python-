'''
    列表
        特点： []  在[]中可以写入不同类型的数据，每个值之间由，分割
             支持角标取值
    元组
        特点： ()  基本和列表相同
    字典
        特点： {}  字典没有索引值，靠键值对取值 {“key” : "value"}
'''

username = input("please input username:")
password = input("please input password:")

# 列表
userlist = ["tom", "jerry"]
passlist = ["123", "456"]

if username in userlist and password in passlist:
    print("welcome "+username+" login")
else:
    print("username or password errno")

# 元组
usertuple = ("lisa", "bob")
passtuple = ("123", "456")

if usertuple in userlist and passtuple in passlist:
    print("welcome "+username+" login")
else:
    print("username or password errno")

# 字典
usermap = {"rose" : "123", "jack" : "456"}


if username in usermap and password == usermap[username]:
    print("welcome"+username+"login")
else:
    print("username or password error")