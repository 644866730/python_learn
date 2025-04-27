import admin.my_admin as a     #包名.模块名
a.info()
# 输出：             导入包时 __init__.py中的文件会被执行
# 版权，杨淑娟
# 讲师，ysj
# 大家好，我叫杨淑娟


print('-'*40)
from admin import my_admin as b
b.info()
#输出：               第二次导入时，__init__.py不会重复执行
# 大家好，我叫杨淑娟

from admin.my_admin import info
info()

# 通配符导入
from admin.my_admin import *
print(name)

if __name__ =='__main__':             #主程序运行
    pass