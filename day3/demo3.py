'''
    不同类型数据的属性
'''
# inta = 12
# print(type(inta))
# print(dir(inta))
# print(inta.__doc__)
# print(inta.bit_length())

# stra = "python"
# print(type(stra))
# print(dir(stra))
# print(stra.__doc__)     #属性
# print(stra.lower())     #小写
# print(stra.upper())     #大写
# print(stra.split("t"))  #分割

# 元组  --- 元组中的值是不可变的
tuplea = ("tom", "jerry")
print(type(tuplea))
print(dir(tuplea))
print(tuplea.index("jerry")) #返回下标


# 列表  --- 成员可变
list = ["tom", "jerry"]
print(type(list))
print(dir(list))
print(list.__doc__)
print(list.index("tom"))    #返回下标
list.append("bob")          #追加
print(list)

# 字典 --- 成员可变
dicta = {"tom":"123", "jerry":"456"}
print(type(dicta))
print(dir(dicta))
print(dicta.keys())     #dict_keys(['tom', 'jerry'])
print(dicta.values())   #dict_values(['123', '456'])
