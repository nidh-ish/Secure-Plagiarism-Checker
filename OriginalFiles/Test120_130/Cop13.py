lis.sort()
print(lis[len(lis)-2])

input()

l = [int(n) for n in input().split()]

highest = -101
second_highest = -101

for n in l:
	if n > highest:
		second_highest = highest
		highest = n
	elif n >= second_highest and n != highest:
		second_highest = n

print(second_highest)

import fileinput

lines = fileinput.input()

N = int(lines[0])
A = list(set(map(int, lines[1].split(" "))))
A.sort()

print(A[len(A)-2])

n = int(input())
a = list(map(int,input().strip().split()))
a.sort()
m = max(a)
while max(a) == m:
    a.remove(m)
    
print(a[len(a)-1])

input()
n = set(map(int, input().split()))
print(sorted(n, reverse=True)[1])

input()
print(sorted(list(set(map(int, input().split(' ')))))[-2])

n = int(input())

numbers_list = set(map(int, input().split(' ')))

numbers_list = list(numbers_list)
numbers_list.sort()

print(numbers_list[-2])

lst = input() == 0 or list(map(int, input().split()))
n = max(lst)
'''
for i in lst:
    if i == n:
        lst.remove(i)
'''
while max(lst) == n:
    lst.remove(n)
print(max(lst))

N = int(input())
A = list(map(int,input().split()))
A.sort()
biggest = A.pop()
i = biggest
while i == biggest:
    i = A.pop()
print(i)

n=int(input())
a=[]
a = [int(x) for x in input().split()]
    
k=set(a)
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
