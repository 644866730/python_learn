#父类A
class fatherA():
    def __init__(self,name):
        self.name =name
    def showA(self):
        print("父类A中的方法")

#父类B
class fatherB():
    def __init__(self,age):
        self.age =age
    def showB(self):
        print("父类B中的方法")

#多继承
class son(fatherA,fatherB):
    def __init__(self, name, age,gender):
        #需要调用两个父类的初始化方法,不能使用super了
        fatherA.__init__(self,name)
        fatherB.__init__(self,age)
        self.gender =gender        
    
son =son("陈美美",20,"女") 
son.showA()
son.showB()