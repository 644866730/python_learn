a=[1,'3',1.34,'6']    # ------------> a:[1, '3', 1.34, '6'] 
b=list('12354')       # ------------> b:['1', '2', '3', '5', '4']

print(a+b)            # ------------>列表相加 
print(a*4)            # ------------>列表相乘
print(a.count('3'))   # ------------>统计列表a中'3'出现的次数
print(a.index(1.34))   # ------------>查找列表a中1首次出现的位置

del a      # ------------>删除列表a


lst=['hello','world','python','php']
# 使用for遍历列表
for item in lst:
    print(item)

# 使用enumerate()遍历列表
for index,item in enumerate(lst,start=10):   #序号从10开始
    print(item)      #index不是索引，是序号


li = ['A', 'B', 'C']
li.append('E')  # 一次只能添加一个元素，并且只能在列表最后
print(li)
# 输出['A', 'B', 'C', 'E']

li = ['A', 'B', 'C', 'E']
li.pop()        # 根据索引进行删除，默认删除最后一个元素,一次只能删除一个
li.pop(0)       # 删除第一位
li.remove('B')  # 删除列表中的值,一次只能删除一个
li.reverse()    # 反转列表元素（从后往前排）


li = ['A', 'B', 'C']
li.insert(0, 'M')  # 在第0位插入M,两个参数
print(li)
# ['M', 'A', 'B', 'C']


# 列表的排序：
li.sort(reverse=True)       #True为降序，False为升序（默认为升序）

li_new=sorted(li,reverse=True)    #sorted排序

# 一维列表的生成式
lst=[item for item in range(90,99)]
print(lst)      #lst=[90, 91, 92, 93, 94, 95, 96, 97, 98]

# 二维列表的建立
lst=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
] 
print(lst)        #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 二维列表的遍历
for row in lst:
    for item in row:
        print(item,end=' ')          #1 2 3 4 5 6 7 8 9

# 二维列表的生成式
lst=[[j for j in range(3)]for i in range(4)]
print(lst)      #[[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]