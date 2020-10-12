# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""

a='Simon Peter John'
b=a.split()
c='*'
for i in range (0,3):
    print(b[i][0],end='')
    print(c*(len(b[i])-1),end='')


"""
"""

list1=['Company 1','Company 2','Company 3']
list2=[]
for i in list1:
    list2.append(i.replace(' ','_'))
print(list2)

"""
"""

list2=[]
list1=[1,2,3,4,5,6]
for a in list1:
    list2.append(str(a))
# c=str(list1)
# list2=['$','$','$','$','$','$']
list3=[str(a)+'$' for a in list1]
print(list3)

"""
"""

list1=['1$', '2$', '3$', '4$', '5$', '6$']
list2=[]
for i in list1:
    list2.append(i.replace('$',''))
print (list2)

"""
"""

list1=[1,2,3,4]
list2=[5,6,7,8]
print(list(zip(list1,list2)))
"""

s="I love you and you love him and who loves who"
a=s.split()

keys=set(a)
values=[0 for i in keys]
d={key:value for key,value in zip(keys,values)}
for i in a:
     d[i]+=1
print(d)