
if (N % 2 == 0 or N > 20) or (N % 2 == 0 and N in range(2, 6)):
    print('Not Weird')

#!/bin/python3

import sys


N = int(input().strip());
if N%2!=0 :
    print("Weird");
elif (N>=6 and N<=20) :
    print("Weird");
else :
    print("Not Weird");


#!/bin/python3

import sys


N = int(input().strip())

if N % 2 == 1:
    print('Weird')
elif N in range(6, 21):    
    print('Weird')
else:
    print('Not Weird')


#!/bin/python3

import sys


N = int(input().strip())
if(N%2 == 0):
    if(N>=2 and N<=5):
        print("Not Weird")
    elif(N>=6 and N<=20):
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")
        



from itertools import groupby

s = input()

print(*[(len(list(g)), int(k)) for k,g in groupby(s)])

from itertools import groupby
s = input().strip()
res = [(len(list(g)),int(k)) for k,g in groupby(s)]
print(" ".join(map(str, res)))

from itertools import groupby

chars=input()
##chars=sorted(input())

for key,group in groupby(chars):
    print(tuple((len(list(group)),int(key))), end=' ')

   
from itertools import groupby

S = input()
for c, X in groupby(S):
    print(tuple((len(list(X)), int(c))),end=' ')

import itertools

s = input()

l = [] 
for k, g in itertools.groupby(s):
	t = (k, len(list(g)))
	l.append(t)

s = ""
for t in l:
	s += "(" + str(t[1]) + ", " + t[0] + ") " 

print(s.rstrip())


from itertools import groupby

in_string = input()

groups = []
for g, s in groupby(in_string):
    groups.append((len([x for x in s]), int(g)))
    
print(*groups, sep=" ")
    
    
    

from itertools import groupby
sample=input()

for x,y in groupby(sample,lambda x: x[0]):

    print ("(%d, %s)"%(len(list(y)),x), end=" ")

#!/usr/bin/env python
# -*- coding: utf-8 -*-
input()
l = sorted([int(i) for i in input().split(' ')], reverse=True)
m = l[0]
for i in range(1, len(l)):
    if l[i] < m:
        print(l[i])
        break


import itertools

groups = itertools.groupby(input())
print( " ".join(["(" + str(len(list(k))) + ", " + g + ")" for g, k in groups ]) )

import itertools
data = input()

groups = []
uniquekeys = []
for k, g in itertools.groupby(data):
    groups.append(list(g))      # Store group iterator as a list
    uniquekeys.append(k)

for g, k in zip(groups, uniquekeys):
    print("({0}, {1})".format(len(g), k), end=" ")

from itertools import groupby
print(*[(len(list(c)), int(k)) for k, c in groupby(input())])

from itertools import combinations_with_replacement,combinations,groupby


s = input().strip()
a = [list(g) for k, g in groupby(s)]
for ele in a:
    print('('+str(len(ele))+', '+str(ele[0])+')',end =' ')


from itertools import groupby

print(' '.join([ '({}, {})'.format(len(list(c)), i) for i, c in groupby(input()) ]))

uncompressed = input()
