if __name__ == "__main__":
    foo(input())
            
    


from itertools import groupby
data=input()
for k, g in groupby(data):
    print((len(list(g)),int(k)),end=" ")

n=int(input())
L=input().split()
l=[int(i) for i in L]
x=[j for i,j in enumerate(l) if j != max(l)]
print(max(x))

from itertools import groupby
from functools import reduce
s = input()
lst = []
for k, v in groupby(s):
    lst.append((len(list(v)), int(k)))
print(reduce(lambda a,b:str(a)+' '+str(b), lst))

s = input() + '/'
curChar = s[0]
curCount = 1
for i in range(1,len(s)):
    if s[i] == curChar:
        curCount += 1
    else:
        print("("+str(curCount)+", "+curChar+")", end = " ")
        curChar = s[i]
        curCount = 1

        

from itertools import groupby
print(*(lambda x: (map(lambda y: (len(y[1]), int((y[0])[0])), map(lambda z: tuple(map(lambda w: tuple(w), z)), x))))(groupby(input().strip())))

from itertools import groupby

chars = input().rstrip()

groups=[]

for k, v in groupby(chars):
    groups.append((len(list(v)), int(k)))
    
print(" ".join(['(%s, %s)' %(k, v) for k, v in groups]))    

chars = input()
from itertools import groupby
lst = [list(g) for k, g in groupby(chars)]

for i in lst:
    print(tuple((len(i),int(i[0]))), end = ' ')

from itertools import groupby
data=input()
for k, g in groupby(data):
    #print(len(list(g)),int(k))
    print ((len(list(g)), int(k)), sep = ", ", end = " ")

from itertools import groupby

s = input().strip()
a = []

for key, count in groupby(s):
    a.append('({}, {})'.format(len(list(count)), key))

print(' '.join(a))

from itertools import groupby

line = input()

for i, j in groupby(line):
    result = (len(list(j)), int(i))
    print(result, end=' ')

from itertools import groupby

S = input()

print(*[(len(list(g)), int(k)) for k, g in groupby(S)], sep=" ")

n = int(input())
line = input().split(' ')
lis = []
for i in line:
    lis.append(int(i))
# lis = [5, 7, 1, 3, 9, 6]
lis.sort()
largest = lis.pop()
while(True):
    try:
        lis.remove(largest)
    except:
        print(lis.pop())
        break


from itertools import groupby
print(*[(len(list(c)), int(k)) for k, c in groupby(input())])

arr = list(input())

result_arr = list()

while arr:
    count = 1
    for j in range(len(arr)-1):
        if len(arr) != 1:
            if arr[j] == arr[j+1]:
                count+=1
                if j == len(arr)-2:
                    result_arr.append((count, int(arr[j]))) 
            else:
                result_arr.append((count, int(arr[j])))
                break

    if len(arr) == 1:
        result_arr.append((count, int(arr[0]))) 

    arr = arr[count:]
            
for item in result_arr:
    print(item, end=" ")
            

import itertools

s = list(input())

res = [(sum(1 for i in g), int(k)) for k, g in itertools.groupby(s)]

print(*res)
    



from itertools import groupby

sample = input()
for key, group in groupby(sample):
    print ((len(list(group)), int(key)), end=' ')


from itertools import groupby
data=input()
for k, g in groupby(data):
    print(tuple((len(list(g)),int(k))),end=' ')

s=input().strip()
from itertools import groupby
res =[]
for k, g in groupby(s):
    res.append('({}, {})'.format(len(list(g)), k))
print(' '.join(res))
    

import itertools
string = list(input())
lists = []
for key, group in itertools.groupby(string):
    lists.append((len(list(group)), int(key)))
for i in lists:
    print(i, end=" ")

from itertools import groupby
ls = input()
for k, g in groupby(ls, lambda x: x):
    print('({0}, {1})'.format(len([a for a in g]), k), end =' ')


from itertools import groupby
s = input()
S = groupby(s)
print(*[(len(list(y)), (int(x))) for x, y in S])

S = input()

count = 1
last = "a"

for i in S:
    if int(i) == last:
        count += 1
    else:
        if last == 'a':
            last = int(i)
            count = 1
        else:
            print(tuple([count, last]), end = ' ')
            last = int(i)
            count = 1
        
        
print(tuple([count, last]))

_ = input()
numbers = set([int(val) for val in input().split()])
print(sorted(numbers)[-2])
