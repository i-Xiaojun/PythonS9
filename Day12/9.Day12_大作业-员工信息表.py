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



def filter_file(condition):
    if '>' in condition:
        li_con = condition.split('>')
        val1 = li_con[0].strip()
        val2 = li_con[1].strip()
        with open('Member_Info.txt') as f:
            for line in f:
                li = line.split(',')
                if int(li[dic[val1]]) > int(val2):
                    # print(line)
                    return li

def show_item(selcect_str):
    item_li = selcect_str.replace('select','').strip().split(',')
    print(item_li)
    return item_li

def show_end(item_li,filter_result):
    for item in item_li:
        print(item)
        print(filter_result[dic[item]],end=' ')

dic = {'id':0, 'name':1, 'age':2, 'phone':3, 'job':4}
sql_str = 'select name,age where age>22'
li_sql = sql_str.strip().split('where')

f = filter_file('age>22')
item = show_item('select name,age ')

show_end(item,f)





# def my_file(filename):
#     with open(filename) as f:
#         for line in f:
#             yield line
#
# def filter_file(condition):
#     if '>' in condition:
#         li_con = condition.split('>')
#         val1 = li_con[0].strip()
#         val2 = li_con[1].strip()
#
#         dic[val1]
#     pass
#
# dic = {'id':0, 'name':1, 'age':2, 'phone':3, 'job':4}
#
# mysql = 'select name,age where age>22'
# li_sql = mysql.strip().split('where')
#
# item = li_sql[0].replace('select','').strip()
# condition = li_sql[1].strip()
#
# print(item,condition)
#
#
#
# my_file('Member_Info.txt')

# def filter_file(item,op,content):
#     f = open('Member_Info.txt')
#     for line in f:
#         li = line.strip().split(',')
#         li_id = li[0]
#         li_name = li[1]
#         li_age = li[2]
#         li_phone = li[3]
#         li_job = li[4]
#         if 'name' in item:
#         if op == '=':
#             pass
#         if op == '>':
#             pass
#         if op == '<':
#             pass
#         if op == 'like':
#             pass
#
#     f.close()
# #
# #
# #
# # def get_name(tiaojian):
# #     pass
#
# def read_input():
#     my_sql = input('>>>')
#     sql_li = my_sql.split('where')
#     print(sql_li)
#     if 'select' in sql_li[0]:
#         item = sql_li[0].split('select')
#         my_select(item[1])
#     else:
#         return print('请以select开头')
#
#
#
# def my_select(s):
#     if s.strip() == '*':
#         return 1
#     else:
#         print(s.strip().split(','))
#         return s.strip().split(',')
#
# read_input()