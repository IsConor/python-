'''
    变量交换
'''

first = input("please input first num:")
second = input("please input second num:")

# 版本1 所有语言的通用思想
# temp = first
# first = second
# second = temp

# 版本2 适合python
first, second = second, first

print("first = "+first)
print("second = "+second)

