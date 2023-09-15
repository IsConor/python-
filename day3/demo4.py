'''
    循环语句: for   while
    break:      立即跳出循环
    continue：  当该语句被执行时，会结束当前循环，开始执行下次循环
'''

import random


# num = 0
# c_choise = random.randint(1, 100)
#
# while num < 10:
#     num += 1
#     p_choise = int(input("please input a number between 1~100: "))
#     if p_choise > c_choise:
#         print("you guess too height")
#     elif p_choise < c_choise:
#         print("you guess too lower")
#     else:
#         print("congratulation you win")
#         break

for item in "python": #字符串
    print("hello"+item)

for item in ["tom", "jerry"]: # 列表
    print("hello"+item)

for item in ("Jack", "Rose"): # 元组
    print("hello"+item)

adict = {"tom":"123", "jerry":"456", "bob":"789"}
for item in adict: # 字典
    print("hello"+adict[item])

sumnub = 0
for item in range(1,11):
    sumnub+=item
    if item == 3:
        break
print(sumnub)

