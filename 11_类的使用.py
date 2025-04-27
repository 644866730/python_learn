# 类的组成和使用
class student():
    #类属性：定义在类中，方法外的变量
    school='西南科技大学'  

    # 初始化方法方法
    def __init__(self,xm,age):  # xm,age是方法的参数，是局部变量，作用域是整个__init__方法
        self.name = xm          # 将局部变量的值赋值给实例属性，实例属性可以在整个类中使用
        self.age = age          # 实例属性名称可以和局部变量相同

    #定义在类中的函数成为方法，自带一个参数self
    def show(self):
        print(f"我叫{self.name},今年{self.age}岁")
    
# 根据图纸可以创建N个对象
stu1 = student("陈美美",22)    #init方法中有两个参数，self是自带参数无需传入
stu2 = student("marry",22)
stu3 =student("玛丽",20)

print(type(stu1))     #----> <class '__main__.student'> 
#用列表存储类，遍历列表
lst=[stu1,stu2,stu3]
for item in lst:         # item是studen类
    item.show()