# 写
def my_write():
    file=open('note.txt','w',encoding='utf-8')
    file.write('伟大中国梦')
    file.close()

# 读
def my_read():
    file=open('note.txt','r',encoding='utf-8')
    result=file.read()
    print(type(result),result)
    file.close()


if __name__=='__main__':
    my_write()
    my_read()
