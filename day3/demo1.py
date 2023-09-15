buf = input("yes/no:")
if "yes" in buf:
    print("yes")
else:
    print("no")

# 索引
arr = "python"
print(arr[0:2])     #显示结束位置之前的内容
print(arr[0:6:1])   #起始位置和步长
print(arr[-1])      #倒数第一个值
print(arr[-1:-4:-1])#从右往左索引，显示结束位置之前的内容
print(arr[-1:-100:-1])
print(arr[:])       #正向索引全部
print(arr[::-1])    #反向索引全部