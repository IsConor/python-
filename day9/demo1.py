'''
    模块的调用
'''
# 导入方式1
# as

# 本质：使用变量名module01关联模块地址
# import module01
#
# module01.func01()

# 导入方式2
# 本质：将指定的成员导入当前模块作用域中
# 小心：导入进来的成员不要和当前模块成员名称相同
# from module01 import MyClass02
# from module01 import func01
#
# func01()
# MyClass02()

# 导入方式3
# 本质：将指定模块的所有成员导入到当前作用域中
# 小心：导入进来的成员和其它模块中的成员冲突
from module01 import *
func01()
MyClass02()