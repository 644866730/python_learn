# 存储和读取一维数据
def my_write():
    # 一维数据可以用列表，元组，或集合
    lst=['张三','李四','王五','陈六']
    with open('student.csv','w',encoding='utf-8')as file:          
        file.write(','.join(lst))         #csv格式是逗号分隔   

def my_read():
    with open("student.csv",'r',encoding='utf-8')as file:
        s=file.read()
        lst=s.split(',')
        print(lst)



# 存储和读取二维数据
def my_write_table():
    lst=[
        ['商品名称', '单价', '采购数量'],
        ['水杯', '98.5', '20'],
        ['鼠标', '89', '100']
    ]
    with open('table.csv','w',encoding='utf-8')as file:
        for item in lst:
            line=','.join(item)
            file.write(line)
            file.write('\n')

def my_read_table():
    data=[]
    with open('table.csv','r',encoding='utf-8')as file:
        lst=file.readlines()      #每一行是列表中的一个元素
        # print(type(lst),lst)
        for item in lst:
            item=item[:len(item)-1]      #去掉每一行的'\n'
            new_lst=item.split(',')
            data.append(new_lst)
    print(data)


if __name__=='__main__':
    my_write()
    my_read()
    my_write_table()
    my_read_table()