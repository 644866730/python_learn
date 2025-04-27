# (1)创建字典
d={ 10:'cat' , 20:'dog' , 30:'pet' , 40:'zoo' }
print(d)

# (2)使用zip创建字典
lst1 = [10,20,30,40]
lst2 = ['cat' ,'dog' ,'pet' ,'zoo' ]
zipobj = zip(lst1 , lst2)    #此时是一个zip对象
d= dict(zipobj)      #转成字典类型
print(d)             #{10: 'cat', 20: 'dog', 30: 'pet', 40: 'zoo'}

# (3)使用参数创建字典
d= dict(cat=10 ,dog=20, pet=30, zoo=40)     #左侧是键，右边是值
print(d)          #{'cat': 10, 'dog': 20, 'pet': 30, 'zoo': 40}

del d     #删除字典


#字典的访问
d= dict(cat=10 ,dog=20, pet=30, zoo=40) 
print(d.keys())    #输出所有的key值
print(d.values())   #输出所有的value值
print(d['cat'])     #10
print(d.get('cat'))    #10

# 字典的遍历1
for item in d.items():
    print(item)      # 得到键和值组成的元组
# ('cat', 10)
# ('dog', 20)
# ('pet', 30)
# ('zoo', 40)   

# 字典的遍历2
for key,val in d.items():
    print(key,'--->',val)
# cat ---> 10
# dog ---> 20
# pet ---> 30
# zoo ---> 40

