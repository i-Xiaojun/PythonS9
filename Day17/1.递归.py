# import sys
# sys.setrecursionlimit(1000000)
#
# n = 0
# def story():
#     global n
#     n += 1
#     print(n)
#     story()
#
# story()

def story():
    print('从前有座山')
    story()
    print('Over')

story()

# RecursionError: maximum recursion depth exceeded while calling a Python object
# 递归错误:超过最大递归深度

