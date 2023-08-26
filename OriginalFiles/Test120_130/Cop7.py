print(tuple([count, last]))

_ = input()
numbers = set([int(val) for val in input().split()])
print(sorted(numbers)[-2])

from itertools import groupby
string = [int(l) for l in list(input())]
tups = [(len(list(k)),i) for i,k in groupby(string)]
print(*tups,sep=' ')
             


from itertools import groupby

data = str(input()).strip()
print(*[(int((len(list(j)))),int(i)) for i,j in groupby(data)])


from itertools import groupby
s = input()
gb = groupby(s)
result = ''
for i, j in gb:
    result = result + '(%s, %s) ' % (len(list(j)), i)
result_2 = result.strip()
print(result_2)

import itertools
for i, j in itertools.groupby(input()):
    print(tuple((len(list(j)), int(i))), end = ' ')

from itertools import groupby
a = input()
print(*[(len(list(g)), int(k)) for k, g in groupby(a)])

from itertools import groupby
data = input()
groups = []
uniquekeys = []
#data = sorted(data, key=keyfunc)
for k, g in groupby(data):
    groups.append(list(g))      # Store group iterator as a list
    uniquekeys.append(k)
for i in range(len(groups)):
    a = (len(groups[i]), uniquekeys[i])
    print("({}, {})".format(a[0], a[1]), end=' ')
    


from itertools import groupby

print(" ".join([str((len(list(g)), int(k))) for k, g in groupby(input().strip())]))

from itertools import groupby
a = input()
for key, group in groupby(a):
    print ((len(list(group)), int(key)), end=' ')

from itertools import *

s = input()
num = [int(k) for k, g in groupby(s)]
num_occ = [len(list(g)) for k, g in groupby(s)]

for i in zip(num_occ, num):
    print(i, end=' ')

input()
A = list(map(int, input().split()))
prev=-1000
cur=A[0]
for i in range(0,len(A)):
    if(A[i]>cur):
        cur=A[i]
for i in range(0,len(A)):
    if(A[i]>prev and A[i]<cur):
        prev=A[i]
print (prev)

num_elements = int(input().strip())
elements = list(set(map(int, (input().split()))))

elements.remove(max(elements))
second_largest = elements.pop(elements.index(max(elements)))
print(second_largest)

n = int(input())
arr = list(map(int,input().split()))
max = -100
for i in range(n):
    if arr[i] > max:
        max = arr[i]     
arr = [x for x in arr if x != max] 
max = -100
for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i] 
        
print(max)        

i=int(input())
lis=list(map(int, input().strip().split(" ")))[:i]
y=max(lis)
while max(lis)==y:
    lis.remove(y)
print(max(lis))

_,x = input(),[int(i) for i in input().split()]
print(max([i for i in x if i != max(x)])) 

n = int(input())
a = list(map(int, input().split()))
maxa = - 1000
sndmaxa = -1000
for i in range(n):
    if(a[i] > maxa):
        sndmaxa = maxa
        maxa = a[i]
    elif(a[i] > sndmaxa and a[i] < maxa):
        sndmaxa = a[i]
