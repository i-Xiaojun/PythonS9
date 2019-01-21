# 装饰器的第一版实现
# import time
#
# def func():
#     print('I`m ABC')
#     time.sleep(0.1)
#
# def mytimer(func):
#     def inner():
#         start = time.time()
#         func()
#         end = time.time()
#         print(end-start)
#     return inner
#
# func = mytimer(func)
# func()

# 装饰器的第二版实现
# import time
#
# def mytimer(func):
#     def inner():
#         start = time.time()
#         func()
#         end = time.time()
#         print(end-start)
#     return inner
#
# @mytimer
# def func():
#     print('I`m ABC')
#     time.sleep(0.1)
#
# func()
#
'''
[问题]
1. mytimer一定需要定义在func之上, 但实际是先写func函数,再写mytimer函数
2.如果跨文件进行调用和定义该如何进行
'''



# 装饰器带参数实现
# def myprint(func):
#     def inner(*args,**kwargs):
#         print('Befor=======')
#         func(*args,**kwargs)
#         print('After*******')
#     return inner
#
# @myprint  #func = myprint(func)
# def func(*args,**kwargs):
#     print([i for i in args])
#
# func(1,2)

# 装饰器带返回值实现
# def myprint(func):
#     def inner(*args,**kwargs):
#         print('Befor=======')
#         ret = func(*args,**kwargs)
#         print('After*******')
#         return ret
#     return inner
#
# @myprint  #func = myprint(func)
# def func(*args,**kwargs):
#     return [i for i in args]
#
# li = func(1,2)
# print(li)
# print(func.__name__)

# 装饰器实现可以查看内置方法
# from functools import wraps
#
# def myprint(func):
#     @wraps(func)
#     def inner(*args,**kwargs):
#         print('Befor=======')
#         ret = func(*args,**kwargs)
#         print('After*******')
#         return ret
#     return inner
#
# @myprint  #func = myprint(func)
# def func(*args,**kwargs):
#     return [i for i in args]
#
# li = func(1,2)
# print(li)
# print(func.__name__)