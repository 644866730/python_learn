import os
print('当前工作路径:',os.getcwd())
print('当前目录下的所有目录和文件', os.listdir())
print('指定目录下的所有目录和文件', os.listdir(r'C:\Users\Kyrie Irving\Desktop\python_test\admin'))
# os.chdir(r'C:\Users\Kyrie Irving\Desktop')    #修改当前工作路径

# os.mkdir('示例文件夹')                   #创建目录
# os.makedirs('示例文件夹/示例1/示例2')     #创建多级目录
# os.rmdir('示例文件夹/示例1/示例2')        #删除目录
# os.removedirs('示例文件夹/示例1')         #删除多级目录
# os.remove('./note_copy.txt')         #删除文件
# os.rename('student.txt','new_student.txt')       #文件重命名

# 遍历目录树,遍历所有目录和文件
for dirs,dirlst,filelst in os.walk(r'C:\Users\Kyrie Irving\Desktop\python_test'):
    print(dirs)
    print(dirlst)
    print(filelst)
    print('--------------------------------`')

import   time
def date_format(longtime):                 #将时间戳转换固定格式
    s=time.strftime('%Y-%m-%d %H:%H:%S',time.localtime(longtime))
    return s

info=os.stat('new_student.txt')       #获取文件信息  
print(info)
print('获取最近访问的时间:',date_format(info.st_atime))
print('文件创建时间:',date_format(info.st_ctime))
print('文件最后一次修改时间:',date_format(info.st_mtime))
print('文件大小(字节):',info.st_size)

# 启动路径下的文件
# os.startfile(r'D:\Anaconda3\python.exe')     
print('-'*40)

#os的path模块
import os.path
print('获取绝对路径:',os.path.abspath('new_student.txt'))
print('判断文件是否存在:',os.path.exists('student.txt'))
print('拼接路径:', os.path.join(r'C:\Users\Kyrie Irving\Desktop\python_test','new_student.txt'))
print('分割文件名和文件后缀名:',os.path.splitext('new_student.txt'))     #元组
print('提取文件名:',os.path.basename(r'C:\Users\Kyrie Irving\Desktop\python_test\new_student.txt'))
print('提取路径名:',os.path.dirname(r'C:\Users\Kyrie Irving\Desktop\python_test\new_student.txt'))
print('判断是否为有效路径:',os.path.isdir(r'C:\Users\Kyrie Irving\Desktop\python_test'))