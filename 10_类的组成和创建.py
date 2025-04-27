# 类的创建
class person():
    pass

class cat():
    pass

person1=person()   # person对象的创建
cat1=cat()         # cat对象的创建

print("--------------------------------------------------------------------------->")


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
    
    # 静态方法
    @staticmethod
    def sm():
        print("这是一个静态方法，不能调用实例属性，也不能使用实例方法")

    #类方法，自带一个cls参数
    @classmethod
    def cm(cls):
        print("这是一个类方法，不能调用实例属性，也不能使用实例方法")

gch = student("关昌浩",22)    #init方法中有两个参数，self是自带参数无需传入

# 类属性,直接使用类名打点调用
print(student.school)

# 实例属性,使用对象名进行打点调用
print(gch.name,'  ',gch.age)             # 关昌浩 22

# 实例方法,使用对象名打点调用
gch.show() 

# 类方法和静态方法,使用类名打点调用
student.sm()
student.cm()