class person():
    def eat(self):
        print('人，吃五谷杂粮')

class cat():
    def eat(self):
        print('猫，喜欢吃鱼')

class dog():
    def eat(self):
        print('狗，喜欢啃骨头')

#这三个类都有一个同名方法，eat
#编写函数
def fun(obj):  # obj是形式参数，现在根本不知道其数据类型
    obj.eat()  # 但是仍然可以通过obj(对象)调用eat方法

#创建三个类的对象
per =person()
cat =cat()
dog =dog()
#调用fun函数
fun(per)
fun(cat)
fun(dog)
