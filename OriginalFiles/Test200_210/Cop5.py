for i in word[1:]:
    if int(i) == x[1]:
        x = (x[0] + 1, int(i))
    else:
        print (x, end = ' ')
        x = (1, int(i))
print (x, end = ' ')


import itertools

S = input()

if len(S) == 1:
    print ((1,int(S[0])))

else:
    n = 0
    
    for i in range(1,len(S)):
        if S[i] == S[i-1]:
            n += 1
        else:
            print ((n+1,int(S[i-1])), end = ' ')
            n = 0
            
print ((n+1,int(S[i])))


from itertools import groupby
print(*[(len(list(c)), int(k)) for k, c in groupby(input())]) #RunLengthCoding

from itertools import groupby
s = input()

print(*[(len(list(g)),int(k)) for k, g in groupby(s)])

from itertools import groupby

data = list(int(item) for item in input())

for k, g in groupby(data):
	t = 0
	for n in g:
		t+= 1
	print(tuple([t, k]), end=" ")

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

