import json
# 准备高维数据，高维数据用字典
lst=[
    {'name':'杨淑娟', 'age':18, 'score':90},
    {'name':'陈美美', 'age':21, 'score':99},
    {'name':'张一一', 'age':19, 'score':85}
]

#编码
s=json.dumps(lst,ensure_ascii=False,indent=4) # ensure_ascii正常显示中文，indent增加数据的缩进，美观用的
print(type(s))        # str
print(s)       

#解码
lst2=json.loads(s)
print(type(lst2))   
print(lst2) 

#编码到文件中
with open('student.txt','w',encoding='utf-8')as file:
    json.dump(lst, file, ensure_ascii=False, indent=4)

#解码到程序
with open('student.txt','r',encoding='utf-8')as file:
    lst3=json.load(file)
    print(type(lst3))     #---->list
    print(lst3)

