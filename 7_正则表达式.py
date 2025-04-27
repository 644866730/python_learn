import re

#match函数使用，从开始匹配
pattern='\d.\d+'   #匹配模式
s='I study python 3.11 every day'
match=re.match(pattern,s,re.I)
print(match)  #None
s1='3.11I study python every day'
match1=re.match(pattern,s1,re.I)
print(match1)   #<re.Match object; span=(0, 4), match='3.11'>
print("匹配的起始位置是：",match1.start())    #0
print("匹配的结束位置是：",match1.end())      #4
print("匹配的数据是：",match1.group())       #3.11

#search函数使用，在整个字符串匹配，但只匹配到第一个的值
pattern='\d.\d+'   #匹配模式
s='I study python 3.11 every day python 2.7 I love you'
match=re.search(pattern,s)
print(match.group)    #3.11,只找到第一个匹配到的值

#findall函数使用，在整个字符串匹配，匹配所有值,结果为列表
pattern='\d.\d+'   #匹配模式
s='I study python 3.11 every day python 2.7 I love you'
match=re.findall(pattern,s)
print(match)    #['3.11', '2.7']




print("------------------------------------------------------->")
# sub()替换字符串函数
pattern='黑客|破解|反爬'
s='我想学习python,想破解一些VIP网站，python可以实现反爬'
new_s=re.sub(pattern,'***',s)
print(new_s)          #我想学习python,想***一些VIP网站，python可以实现***

#split()字符分割函数
s2='https://www.baidu.com/s?wd=ysj&ie=utf-8&tn=15007414_2_pg'
pattern2='[?|&]'
lst=re.split(pattern2,s2)
print(lst)      #['https://www.baidu.com/s', 'wd=ysj', 'ie=utf-8', 'tn=15007414_2_pg']