class student():
    # 首位双下划线,特殊的方法，一般是系统定义的名字
    def __init__(self,name,age,gender):
        self._name = name   #self._name是单下划线开头，受保护实例属性，只能类本身和子类访问
        self.__age =age     #self.__name是双下划线开头，私有的实例属性，只能类本身访问
        self.gender =gender  #普通实例属性，类的内部，外部，子类都可以访问

    def _fun1(self):     #受保护方法
        print("只能类本身和子类访问")

    def __fun2(self):   #私有方法
        print("只能类本身")

    def show(self):     #普通实例方法
        self._fun1()    # 类本身访问受保护方法
        self.__fun2()   # 类本身访问私有方法
        #类本身访问受保护实例属性和私有实例属性
        print(f"我叫{self._name},今年{self.__age}岁")    

stu= student("陈美美",20,'女')
# 当前处于类的外部
# 受保护的可以访问
print(stu._name)   
stu._fun1()
# stu.__age   stu.__fun2    私有的不可以这样访问,要用特定格式访问
# 对象名._类名__私有      非常不建议这样使用
print(stu._student__age)
stu._student__fun2()

print(dir(stu))      #dir可以查看类的所有组成