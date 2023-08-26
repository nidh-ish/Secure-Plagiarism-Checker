from itertools import groupby

print (' '.join([ str((len(list(y)), int(x))) for x, y in groupby(input().strip()) ]))


import itertools
s = input()

for key, group in itertools.groupby(s):
    print((len(list(group)), int(key)), end=" ")

n = int(input())
a = set(map(int,input().split(' ')))
b = list(a)
b.sort()
n = len(b)
print(b[n-2])

from itertools import groupby
s = input().strip()
l = []
for k,g in groupby(s):
    l.append((len(list(g)), int(k)))
print(*l)

import itertools
S = input()
groups=[]
for k,g in itertools.groupby(S):
    groups.append((len(list(g)),int(k)))
print(" ".join([str(g) for g in groups]))

import itertools
s = input()
a = [(len(list(g)),int(k)) for k,g in itertools.groupby(s)]
print(" ".join(map(str,a)))

from itertools import groupby
data = input()
for k, g in groupby(data):
    print(tuple((len(list(g)),int(k))),end=' ')

from itertools import groupby
s = input()
print(*[(len(list(c)), int(k)) for k, c in groupby(s)])

import itertools
s = list(input())
print(" ".join(map(lambda a: str((len(list(a[1])), int(a[0]))), itertools.groupby(s))))

from itertools import *

k = input()

ll = [list(g) for k,g in groupby(k)]

for i in ll:
    qq = (len(i), (int(i[0])))
    print(qq, end=' ')




from itertools import groupby

for i in [(len(list(g)),int(k)) for k, g in groupby(input().strip())]:
    print(i,end=" ")


input_str = input()
output_lst = []

count = 0
prev_elem = ''

for elem in input_str :
    
    if prev_elem == '' :
        prev_elem = elem
        count += 1
        
    elif prev_elem != elem : 
        output_lst.append((count,(int)(prev_elem)))
        prev_elem = elem
        count = 1
        
    else :
        count += 1

output_lst.append((count,(int)(prev_elem)))
        
for elem in output_lst :
    print(elem,end=' ')


from itertools import groupby


def compress(text):
    res = ''
    for key, group in groupby(text, lambda x: x):
        res = res + '({1}, {0})'.format(key, len(list(group))) + ' '
    print(res)


text = input()
compress(text)


N = int(input())
myset = set(int(i) for i in input().strip().split())
print(sorted(myset)[-2])

from itertools import groupby
s = input()
myList = []
for k,g in groupby(s):
    myList.append((len(list(g)),int(k)) )

print(*myList)




from itertools import groupby

seq = input().strip()
for x, y in groupby(seq):
    print((len(list(y)), int(x)), end=" ")

from itertools import groupby
for i,j in groupby(input()):
    print("({0}, {1})".format(len(list(j)),int(i)),sep=' ',end=' ')
    

from itertools import groupby;
s = input().strip();

for key,group in groupby(s,key=None):
    print("("+str(len(list(group)))+", "+str(key)+") ",end="",sep=" ");

import itertools
s = input()
print(" ".join(["({}, {})".format(len(list(g)), k) for k,g in itertools.groupby(s)]))

from itertools import groupby
print(*[(len(list(c)),int(k)) for k,c in groupby(input())])

import itertools as it

s = input()

print(' '.join([ str( (len(list(v)), int(k)) ) for (k, v) in it.groupby(s) ]))
