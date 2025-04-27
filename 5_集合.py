# 集合的创建
s = {10,20,30,40}

# set(可迭代对象)
s = set()  #创建一个空集合
s = set("helloworld")
s = set([10,20,30])
s = {}   #这个创建的是一个空字典

A = {10,20,30,40,50}
B = {30,40,50,60,70}
print(A & B)    #{40, 50, 30}
print(A | B)    #{70, 40, 10, 50, 20, 60, 30}
print(A ^ B)    #{20, 70, 10, 60}
print(A - B)    #{10, 20}



S={10,20,30}
S.add(100)         #添加
S.remove(20)       #删除
s.clear()          #清空

A = {10,20,30,40,50}
# 遍历1
for item in A:
    print(item)
# 遍历2
for index,item in enumerate(A):    #index是序号，不是索引，集合无序
    print(index,'--->',item)

# 集合的生成式
s={item for item in range(90,99) if item%2==0}
print(s)      #s={96, 98, 90, 92, 94}    