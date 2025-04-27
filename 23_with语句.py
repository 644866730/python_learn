# 语句：with open() as file
# with语句会自动关闭文件

def write_fun():
    with open('note.txt','w',encoding='utf-8') as file:
        file.write('2022北京冬奥会')

def read_fun():
    with open('note.txt','r',encoding='utf-8') as file:
        print(file.read())

def copy(src_file,target_file):
    with open(src_file,'r',encoding='utf-8') as file1:
        with open(target_file,'w',encoding='utf-8') as file2:
            file2.write(file1.read())

if __name__=='__main__':
    write_fun()
    read_fun()
    copy('note.txt','note_copy.txt')