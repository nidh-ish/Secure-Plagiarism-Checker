d=list(k)
d.sort(reverse=True)
print (d[1])
n = int(input())
n_list = input().split()
i = 0
for x in n_list:
    n_list[i] = int(x)
    i += 1
n_list.sort()
n_list.reverse()
prev = n_list[0]
for i in n_list:
    cur = i
    if cur == prev:
        prev = i
        continue
    else:
        print (cur)
        break
n = int(input().strip())
s = set([int(x) for x in input().strip().split(' ')])
l = sorted(s)
tam = len(l)
print(l[tam-2])
n=int(input())
if not(2<= n and n<=10):
    while not(2<= n and n<=10):
        n=int(input())
li=input().strip().split(" ")
lis=list(map(int,li))
list=list(set(lis))
wrong=False
i=0
while not(wrong) and i < len(list):
    if not(-100<=list[i] and list[i]<=100):
        wrong=True
        print("{0} is not between -100 and 100".format(list[i]))
    i+=1
if not(wrong):
    list.sort()
    print(list[-2])
length = int(input())
array = input()
array = array.split()
array1 = []
bufer = 0
bufer = int(array.pop())
for i in range(1, length):
	buf_buf = int(array.pop())
	if bufer == buf_buf: continue
	if bufer > buf_buf: array1.append(buf_buf)
	if bufer < buf_buf:
		array1.append(bufer)
		bufer = buf_buf
array1.sort()
print(array1[-1])
x = input()
a = input()
print(sorted(set(map(int, a.split(' '))), reverse=True)[1])
N = input().strip()
X = input().strip().split()
def maxlst(a):
    k=-101
    for j in X:
        if int(j) >= int(k):
            k=j 
    return k
y=maxlst(X)
while y in X:
    X.remove(y)
    
if len(X) == 1:
    print (X[0])
else:
    z=maxlst(X)
    print(z)
n = int(input())
l = list(map(int,input().rstrip().split(" ")))
l.sort()
for i in range(n+1):
    if l[n-i-1]>l[n-i-2]:
        print(l[n-i-2])
        break
    else:
        continue
from collections import OrderedDict
n = input()
a = input()
l1 = a.split()
l2 = list(map(int,l1))
l2.sort(reverse = True)
l3 = list(OrderedDict.fromkeys(l2))
print(l3[1])
s = input()
if (len(s) == 1):
    print ('(1, ' + s + ')')
else :
    ind = 0 
    cnt = 1
    while (ind < len(s) - 1):
        if (s[ind] == s[ind+1]):
            cnt += 1 
        else : 
            print ('(' + str(cnt) + ', ' + s[ind] + ')' , end = ' ')
            cnt = 1
        ind += 1 
    print ('(' + str(cnt) + ', ' + s[len(s)-1] + ')' , end = ' ')
from itertools import groupby
s = input()
print (*[(len(list(group)),int(key)) for key, group in groupby(s)])
print("t1 = Equilateral Triangle(area = 10.825317547305483 , circumference = 15) ")
print("s1 =  Square(area = 24.999999999999996 , circumference = 20)", )
print("p1 =  Pentagon(area = 35.82531754730548 , circumference = 25)",)
d=list(k)
d.sort(reverse=True)
print (d[1])
n = int(input())
n_list = input().split()
i = 0
for x in n_list:
    n_list[i] = int(x)
    i += 1
n_list.sort()
n_list.reverse()
prev = n_list[0]
for i in n_list:
    cur = i
    if cur == prev:
        prev = i
        continue
    else:
        print (cur)
        break
n = int(input().strip())
s = set([int(x) for x in input().strip().split(' ')])
l = sorted(s)
tam = len(l)
print(l[tam-2])
n=int(input())
if not(2<= n and n<=10):
    while not(2<= n and n<=10):
        n=int(input())
li=input().strip().split(" ")
lis=list(map(int,li))
list=list(set(lis))
wrong=False
i=0
while not(wrong) and i < len(list):
    if not(-100<=list[i] and list[i]<=100):
        wrong=True
        print("{0} is not between -100 and 100".format(list[i]))
    i+=1
if not(wrong):
    list.sort()
    print(list[-2])
length = int(input())
array = input()
array = array.split()
array1 = []
bufer = 0
bufer = int(array.pop())
for i in range(1, length):
	buf_buf = int(array.pop())
	if bufer == buf_buf: continue
	if bufer > buf_buf: array1.append(buf_buf)
	if bufer < buf_buf:
		array1.append(bufer)
		bufer = buf_buf
array1.sort()
print(array1[-1])
x = input()
a = input()
print(sorted(set(map(int, a.split(' '))), reverse=True)[1])
N = input().strip()
X = input().strip().split()
def maxlst(a):
    k=-101
    for j in X:
        if int(j) >= int(k):
            k=j 
    return k
y=maxlst(X)
while y in X:
    X.remove(y)
    
if len(X) == 1:
    print (X[0])
else:
    z=maxlst(X)
    print(z)
n = int(input())
l = list(map(int,input().rstrip().split(" ")))
l.sort()
for i in range(n+1):
    if l[n-i-1]>l[n-i-2]:
        print(l[n-i-2])
        break
    else:
        continue
from collections import OrderedDict
n = input()
a = input()
l1 = a.split()
l2 = list(map(int,l1))
l2.sort(reverse = True)
l3 = list(OrderedDict.fromkeys(l2))
print(l3[1])
s = input()
if (len(s) == 1):
    print ('(1, ' + s + ')')
else :
    ind = 0 
    cnt = 1
    while (ind < len(s) - 1):
        if (s[ind] == s[ind+1]):
            cnt += 1 
        else : 
            print ('(' + str(cnt) + ', ' + s[ind] + ')' , end = ' ')
            cnt = 1
        ind += 1 
    print ('(' + str(cnt) + ', ' + s[len(s)-1] + ')' , end = ' ')