# import my_info     导入整个模块
# print(my_info.name)     需要打点调用

# import my_info as a     导入整个模块并重命名
# print(a.name)

# from my_info import name    导入模块中的某个变量
# print(name)

# from my_info import info    导入模块中的某个函数
# info()

# 通配符导入整个模块，不需要打点调用了
from my_info import *
print(name)
info()

# 同时导入多个模块
import math,time,random
