'''
    while 循环
        while + 条件
            子语句
'''

# 1~10 偶数和
i = 0
sum = 0
while i < 10:
    i += 1
    if i % 2:
        continue
    sum += i
print(sum)