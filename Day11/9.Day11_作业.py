# 1.编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件）, 要求登录成功一次，后续的函数都无需再输入用户名和密码
# 2.编写装饰器，为多个函数加上记录调用功能，要求每次调用函数都将被调用的函数名称写入文件
# 进阶作业(选做)：
# 1.编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果
# 2.为题目1编写装饰器，实现缓存网页内容的功能：
# 具体：实现下载的页面存放于文件中，如果文件内有值（文件大小不为0），就优先从文件中读取网页内容，否则，就去下载，然后存到文件中

# 1.编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件）, 要求登录成功一次，后续的函数都无需再输入用户名和密码
def login(func):
    def inner(*args,**kwargs):
        # f = open('UserDB.txt')
        # for line in f:
        #     print(line.strip())
        # f.close()
        username = input('Pls input username')
        password = input('Pls input password')
        if username == 'admin' and password == '123':
            print('登录成功')
            ret = func(*args,**kwargs)
            return ret
        else:
            print('登录失败')
    return inner

@login
def func1():
    print('Welcome Func1')

@login
def func2():
    print('Welcome Func2')

def my_func():
    while True:
        num = input('Pls choice: ')
        if num == '1':
            func1()
            return 1
        elif num == '2':
            func2()
            return 2
        elif num == 'q':
            return 'Bye'
        else:
            print('Pls retry: ')

func1()
func2()