try:     #可能出现异常的代码
    num1= int(input("请输入被除数:"))
    num2= int(input("请输入除数:"))
    result=num1/num2

except ZeroDivisionError:
    print("除数不能为0")

except ValueError:
    print("不能输入字符")

except BaseException:      #最大的异常类型
    print("未知异常")

else:
    print(result)


try:
    score=eval(input("请输入分数："))
    if score>=0 & score<=100:
        print("分数:",score)
    else:
        raise Exception("分数不正确")
except Exception as e:
    print(e)