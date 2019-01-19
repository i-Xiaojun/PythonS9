# dic = {'k1':10,'k2':102,'k3':101}
# print(max(dic,key=lambda k:dic[k]))

t1 = (('a'),('b'))
t2 = (('c'),('d'))
# z=zip(t1,t2)
# for i in z:
#     print(i)
z = lambda a,b:zip(a,b)
print(z(t1,t2))

#add = lambda x,y : x+y
#print(max)
dic = {'k1':10,'k2':102,'k3':103}
print(max(dic,key=lambda k:dic[k]))