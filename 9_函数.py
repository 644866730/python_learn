# 函数的定义
def get_sum(n,m):   # n,m是形式参数
    s=0
    for i in range(n,m+1):
        s+=i
    print(f"{n}到{m}的累加和为{s}")
    return s

# 函数的调用
# 位置传参
sum =get_sum(1,100)     # 1,100是实际参数

# 关键字传参
sum =get_sum( m=100, n=1)


# 默认传参，调用时可以不用传参
def get_sum1(n=1,m=100):   # n,m是形式参数
    s=0
    for i in range(n,m+1):
        s+=i
    print(f"{n}到{m}的累加和为{s}")
    return s
sum= get_sum1()


# 个数可变位置参数
def fun(*para):
    print(type(para))
    for item in para :
        print(item)

fun(10,20,30,40)        # <class 'tuple'>   10 20 30 40
fun([10,20,30,40])      # <class 'tuple'>   [10, 20, 30, 40]
fun(*[10,20,30,40])     #会将列表解包传进去，10 20 30 40



# 个数可变的关键字参数
def fun1(**para):
    print(type(para))
    for key,value in para.items() :
        print(key,"---->",value)

fun1(a=10,b=20,c=30,d=40)      
# <class 'dict'>
# a ----> 10
# b ----> 20
# c ----> 30
# d ----> 40 
d= { 'a':10 , 'b':20, 'c':30}
fun1(**d)       #对字典进行系列解包
 

# 函数有多个返回值,返回类型为元组
def get_sum(num):
    s=0
    odd_sum=0
    even_sum=0
    for i in range(1,num+1):
        if  (i % 2) !=0:
            odd_sum+=i
        else:
            even_sum+=i
        s+=i
    return odd_sum,even_sum,s

result=get_sum(10)
print(type(result),'----',result)  # <class 'tuple'> ---- (25, 30, 55)
a,b,c=get_sum(10)    
print(a,b,c,sep='----')      # 25----30----55



# 递归函数,斐不拉契数列
def fibon(n):
    if n==1 or n==2:
        return 1
    else:
        return fibon(n-1)+fibon(n-2)

for i in range(1,9):
    print(fibon(i))

