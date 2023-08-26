compressed = list()

i = 0
count = 1

while i < len(uncompressed):
    
    if i == len(uncompressed)-1:
        compressed.append((count, int(uncompressed[i])))
        break
    
    if uncompressed[i] == uncompressed[i+1]:
        count += 1
    else:
        compressed.append((count, int(uncompressed[i])))
        count = 1
    i += 1

for i in compressed:
    print(i, end=" ")

from itertools import groupby
a = input()
for key, group in groupby(a):
    print ((len(list(group)), int(key)), end=' ')

from itertools import groupby
s = input()
for key,group in groupby(s):
    print((len(list(group)),int(key)),end = ' ')



import itertools
string = input()
groups = []
uniquekeys = []
data = list(string)
for k, g in itertools.groupby(data):
    groups.append(list(g))      # Store group iterator as a list
    uniquekeys.append(k)
for i in groups:
    x = tuple([len(i),int(i[0])])
    print(x,end=' ')
print()

from itertools import groupby

res = []
for k, g in groupby(input()):
    res.append((len(list(g)),int(k)))
    
print(*res)

a = int(input())
s = set([int(x) for x in input().split(" ")])
l = sorted(list(s))

print(l[-2])

import itertools

print(" ".join(["(%d, %s)"%(len(list(g)), k) for k, g in itertools.groupby(input())]))

word = input()
x = (1, int(word[0]))
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


#https://www.hackerrank.com/challenges/compress-the-string
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
