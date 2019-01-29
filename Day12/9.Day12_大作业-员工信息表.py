# 员工信息表
# 文件存储格式如下：
# id，name，age，phone，job
# 1,Alex,22,13651054608,IT
# 2,Egon,23,13304320533,Tearcher
# 3,nezha,25,1333235322,IT
#
# 现在需要对这个员工信息文件进行增删改查。
#
# 不允许一次性将文件中的行都读入内存。
#
# 3.1 可以进行查询，支持三种语法：
# select 列名1，列名2，… where 列名条件
# 支持：大于小于等于，还要支持模糊查找。
# 示例：
# select name, age where age>22
# select * where job=IT
# select * where phone like 133
# 进阶选做
# 3.2 可创建新员工记录，id要顺序增加
# 3.3 可删除指定员工记录，直接输入员工id即可
# 3.4 修改员工信息
# 语法：set 列名=“新的值” where 条件
# #先用where查找对应人的信息，再使用set来修改列名对应的值为“新的值”
#
# 注意：要想操作员工信息表，必须先登录，登陆认证需要用装饰器完成
# 其他需求尽量用函数实现

# 第一版################################################################
# def filter_file(condition):
#     if '>' in condition:
#         li_con = condition.split('>')
#         val1 = li_con[0].strip()
#         val2 = li_con[1].strip()
#         with open('Member_Info.txt') as f:
#             for line in f:
#                 li = line.split(',')
#                 if int(li[dic[val1]]) > int(val2):
#                     # print(line)
#                     yield li
#
# def show_item(selcect_str):
#     item_li = selcect_str.replace('select','').strip().split(',')
#     # print(item_li)
#     return item_li
#
# def show_end(item_li,filter_result):
#     for line in filter_result:
#         for col in item_li:
#             print(line[dic[col]],end=' ')
#         print('')
#
#
# dic = {'id':0, 'name':1, 'age':2, 'phone':3, 'job':4}
# sql_str = 'select name,age where age>22'
# li_sql = sql_str.strip().split('where')
#
# f = filter_file('age>22')
# # for i in f:
# #     print(i)
# item = show_item('select name,age ')
#
# show_end(item,f)


# 第二版################################################################
def open_file(filename):
    with open(filename) as f:
        for line in f:
            li = line.split(',')
            yield li

def filter_file(condition):
    if '>' in condition:
        li_con = condition.split('>')
        val1 = li_con[0].strip()
        val2 = li_con[1].strip()
        for li in open_file('Member_Info.txt'):
            if int(li[dic[val1]]) > int(val2):
                yield li

def show_item(selcect_str):
    item_li = selcect_str.replace('select','').strip().split(',')
    # print(item_li)
    return item_li

def show_end(item_li,filter_result):
    for line in filter_result:
        for col in item_li:
            print(line[dic[col]],end=' ')
        print('')


dic = {'id':0, 'name':1, 'age':2, 'phone':3, 'job':4}
sql_str = 'select name,age where age>22'
li_sql = sql_str.strip().split('where')

f = filter_file('age>22')

item = show_item('select name,age ')

show_end(item,f)
