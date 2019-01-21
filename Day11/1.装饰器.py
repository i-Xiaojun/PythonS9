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

import time

def func():
    print('I`m ABC')
    time.sleep(0.1)

def mytimer():
    #def inner():
        start = time.time()
        func()
        end = time.time()
        print(end-start)
    #return inner


func = mytimer()
func()