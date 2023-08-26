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

print(sndmaxa)

n = input()
arr = [int(i) for i in input().split()]
firstMax = max(arr)
print(max([i for i in arr if i != firstMax]))

N = int(input())
lyst = [int(x) for x in input().split(' ')]
print(sorted(set(lyst))[-2])


input()
l = list(map(int,input().split()))

a = max(l)
while a in l:
    l.remove(a)
print(max(l))

N = int(input())
array = list(map(int, input().split()))

max_array = max(array)

bill = -101
for a in array:
    if a < max_array and a > bill:
        bill = a

print(bill)
        

input()
a = set([int(i) for i in input().split()])
print(list(sorted(a))[-2])

import heapq
a=input()
el=input()
el=el.split()
el=list(map(int,el))
el=[x for x in el if x!= max(el)]
print(max(el))

N = int(input())
tmp = list(input().split())
nlist = list(map(int,tmp))
del(tmp)
nlist.sort()
for i in range(N-1,0,-1):
    if nlist[i]>nlist[i-1]:
        print(nlist[i-1])
        break

input()
s = set(map(int, input().split(" ")))
m = max(list(s))
s.remove(m)
print(max(list(s)))


n = int(input())
nums = map(int, input().split()) 
print (sorted(list(set(nums)))[-2])

n = int(input())
A = list(set(map(int, input().split())))
A.sort()
print(A[len(A)-2])

import sys
input()
a = list(map(int, input().split()))
m2 = m1 = -sys.maxsize
for i in a:
    if i > m1:
        if i > m2:
            m1, m2 = m2, i
        elif i < m2:
            m1 = i
print(m1)


#!/bin/python3

import sys


m = int(input().strip())
marr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
mlist = list(marr)

mlist.sort(reverse=True)

for item in mlist:
    if item != mlist[0]:
        print(item)
        break



N, A = int(input()), [int(number) for number in input().split()]
largest_number = -101
second_largest_number = -101

for x in A:
    if x > largest_number:
        second_largest_number = largest_number
        largest_number = x
    elif x < largest_number and x > second_largest_number:
        second_largest_number = x
    
print(second_largest_number)

n = int(input())
inp = input()
lis = [int(i) for i in inp.split()]
s = set(lis)
lis = list(s)
