# 装饰器带参数实现
# FLAG = False
# def wrap_flag(FLAG):
#     def wrap(func):
#         def inner(*args,**kwargs):
#             if FLAG:
#                 print('-----Before------')
#             ret = func(*args,**kwargs)
#             if FLAG:
#                 print('======After=======')
#             return ret
#         return inner
#     return wrap
#
# @wrap_flag(FLAG)
# def func():
#     print('I`m Func')
#
# func()

# 多个装饰器装饰同一个函数
# def wrap1(func):
#     def inner(*args,**kwargs):
#         print('1-----Before------1')
#         ret = func(*args,**kwargs)
#         print('1======After=======1')
#         return ret
#     return inner
#
# def wrap2(func):
#     def inner(*args,**kwargs):
#         print('2-----Before------2')
#         ret = func(*args,**kwargs)
#         print('2======After=======2')
#         return ret
#     return inner
#
# @wrap1
# @wrap2
# def func():
#     print('I`m Func')
#
# func()