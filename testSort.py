#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import numpy as np
a = np.array([0,1,3,2,6,4,5])
b = np.array([0,1,2,3,4,5,6])
index = np.lexsort((b, a))

sorted_index = np.argsort(a)

print(index)
print(sorted_index)

c  = a[index]
print(c)
#name sort by second word
[i for i,v in sorted(enumerate(['Vincent', 'Alex', 'Bill', 'Matthew']), key=lambda x:x[1])]

x =[1,2,3]
y =[-4,5,6]
z = list(map(abs,y))
print(z)