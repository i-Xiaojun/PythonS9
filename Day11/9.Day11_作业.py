# 1.编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件）, 要求登录成功一次，后续的函数都无需再输入用户名和密码
# 2.编写装饰器，为多个函数加上记录调用功能，要求每次调用函数都将被调用的函数名称写入文件
# 进阶作业(选做)：
# 1.编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果
# 2.为题目1编写装饰器，实现缓存网页内容的功能：
# 具体：实现下载的页面存放于文件中，如果文件内有值（文件大小不为0），就优先从文件中读取网页内容，否则，就去下载，然后存到文件中

# 1.编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件）, 要求登录成功一次，后续的函数都无需再输入用户名和密码
# FLAG = True  # Ture为需要登录认证
# def login(func):
#     def inner(*args,**kwargs):
#         global FLAG
#         if FLAG:
#             username = input('Pls input username: ')
#             password = input('Pls input password: ')
#             with open('UserDB.txt','r') as f:
#                 li = f.readline().split(',')
#                 if username == li[0] and password == li[1]:
#                     print('登录成功')
#                     ret = func(*args,**kwargs)
#                     FLAG = False
#                     return ret
#                 else:
#                     print('登录失败')
#         else:
#             ret = func(*args, **kwargs)
#             return ret
#     return inner
#
# @login
# def func1():
#     print('Welcome Func1')
#
# @login
# def func2():
#     print('Welcome Func2')
#
# func1()
# func2()

# 2.编写装饰器，为多个函数加上记录调用功能，要求每次调用函数都将被调用的函数名称写入文件
# from functools import wraps
#
# def record(func):
#     @wraps(func)
#     def inner(*args,**kwargs):
#         pass
#         ret = func()
#         with open('record.txt','a+') as f:
#             # print(func.__name__)
#             f.write(func.__name__+'\n')
#         return ret
#     return inner
#
# @record
# def func1():
#     print('I`m Func1')
#
# @record
# def func2():
#     print('I`m Func2')
#
# func1()
# func2()