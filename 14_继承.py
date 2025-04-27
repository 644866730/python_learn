# 父类
class person():   #默认继承object类
    def __init__(self,name,age):
        self.name =name
        self.age =age
    def show(self):
        print(f"我叫{self.name},今年{self.age}岁")

#子类1 student继承person类
#子类可以继承父类公有的和受保护的
class student(person):
    def __init__(self, name, age,id):
        super().__init__(name, age)     #调用父类的初始化方法给name和age赋值
        self.id =id                   #自己的独有特征自己赋值

#子类2 doctor类
class doctor(person):
    def __init__(self, name, age,department):
        super().__init__(name, age)   
        self.department =department

stu=student("陈美美",20,'5120215683')
stu.show()

doc=doctor("张一一",32,"外科")
doc.show()

