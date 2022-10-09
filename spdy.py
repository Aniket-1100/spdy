#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Aniket Pratap Singh
#
# Created:     09-10-2022
# Copyright:   (c) Aniket Pratap Singh 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

x = 'hi everyone'
print(x.upper())

y = 'HI EVERYONE'
print(y.lower())

a = ' lets study python'
print(a.strip())

b = 'Hello World'
print(x.split())

c = 'hello'
print(c.replace("h","a"))

d = 'hello'
e = 'world'
f = d+""+e

print(5>2)
print(5<3)

l = [10,20,30,40,50]
print(l)
l[2] = 'hello'
l[1] = 90
print(l)


i = [10,20,30,40,50]
i[1:3] =['hi','everyone']
print(l)

p = [10,20,30,40,50]
p.insert(2,40)
print(p)

q = [10,20,30]
q.append(40)
print(q)

l1 = [10,20,30]
l2 = [40,50,60]
l1.extend(l2)
print(l1)

z = ['john','peter','sam']
z.remove('sam')
print(z)