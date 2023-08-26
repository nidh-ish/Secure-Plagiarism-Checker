from itertools import groupby
S = input()
group = [(len(list(cgen)), int(c)) for c,cgen in groupby(S)]
print(*group, sep=" ")

import itertools

print(*map(lambda x: (len(list(x[1])), int(x[0])) , itertools.groupby(input())), sep=' ')

import itertools

S = str(input())
S = map(int,list(S))


for k,g in itertools.groupby(S):
    print ((len(list(g)),k),end=' ')
    #print(elem[0],list(elem[1]))

st = input()

output = ""
ch_current = st[0]
count = 0
for ch in st:
	if ch == ch_current:
		count += 1
	else:
		output += "(" + str(count) + ", " + str(ch_current) + ") "
		count = 1
		ch_current = ch
output += "(" + str(count) + ", " + str(ch_current) + ") "
print(output)

n = input().strip()
m = [int(temp) for temp in input().strip().split()]
for i in range(m.count(max(m))):
    m.remove(max(m))
print(max(m))

from itertools import groupby

s = input()
res = groupby(s)
for char, occ in res:
    print('(%r, %r)' % (len(list(occ)), int(char)), end=" ")

from itertools import groupby
string = input()
def group_counter(s):
    return [(len(list(b)),int(a)) for a,b in groupby(s)] # groups sequential units and counts how many times they occur
print(' '.join(list(map(str,group_counter(string)))))    # -- list(b) is the sequence of the group character ['a', 'a', 'a']

import itertools
S = input()
for a, b in itertools.groupby(S):
    print((len(list(b)), int(a)), end=' ')

from itertools import groupby

S = input()
for x in groupby(S):
    print('(%s, %s)' % (len(list(x[1])), x[0]), end=' ')

from itertools import groupby

nums = [int(i) for i in input()]

print(*[(sum(map(lambda x: 1, g)), k) for k, g in groupby(nums)])

import itertools
a = input()
a = [int(aa) for aa in a]
res = []
for k, v in itertools.groupby(a):
    res.append((len(list(v)), k))

print(' '.join(map(str, res)))

# Compress the String!
from itertools import groupby
s = input().strip()
# print([(int(k), len(list(v))) for (k,v) in list(groupby(s))])
for k, v in groupby(s):
  print((len(list(v)), int(k)), end=" ")


from itertools import groupby as g
s= input()
for i, j in g(s):
    print((len(list(j)), int(i)), end=' ')

import itertools
s = input() 
print(*[(len(list(b)), int(a)) for a,b in itertools.groupby(s)])

from itertools import groupby

S = input()

print(" ".join([str((len(list(g)), int(k))) for k, g in groupby(S)]))
 


N = int(input())
A = input().split()
A = list(map(int,A))
q = max(A)
while max(A)==q:
    A.remove(max(A))
    
print(max(A))

from itertools import groupby


def RLE(s):
    return [(len(list(g)), k) for k, g in groupby(s)]


def main():
    s = input()

    r = RLE(s)
    for i in r:
        print("({0}, {1})".format(i[0], i[1]), end=" ")
    print()

    
if __name__ == '__main__':
    main()


from itertools import groupby

s = input()

tuples = []
for k, g in groupby(s):
    occs = len(list(g))
    tuples.append((occs, int(k)))

print(' '.join([str(t) for t in tuples]))



from itertools import groupby
print( *[  ( len(list(c)), int(k) ) for k, c in groupby(input())  ] )

from itertools import groupby
data=input()
for k, g in groupby(data):
    print(tuple((len(list(g)),int(k))),end=' ')


from itertools import groupby
S = input().strip()

groups = []
for key, group in groupby(S):
    groups.append((len(list(group)), int(key)))

print(*groups, sep=' ')

from itertools import groupby
stri = list(map(int, input()))

groups = []
uniquekeys = []
for k, g in groupby(stri):
    groups.append(list(g))
    uniquekeys.append(k)

l = [(len(i), j) for i, j in zip(groups, uniquekeys)]
for i in l:
    print(i, end=" ")

from itertools import groupby

my_list = map(int, input())

groups = groupby(my_list)

print(" ".join(list("({0}, {1})".format(len(list(v)), k) for k, v in groups)))


from itertools import groupby
a = input()
for key, group in groupby(a):
    print ((len(list(group)), int(key)), end=' ')

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
