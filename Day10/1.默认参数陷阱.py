# def defult_param(a,l=[]):
#     l.append(a)
#     print(l)
#
# defult_param('harry')
# defult_param('boy')

def defult_param(a, l={}):
    #l.append(a)
    l[a]='v'
    print(l)

defult_param('harry')
defult_param('zhou')
