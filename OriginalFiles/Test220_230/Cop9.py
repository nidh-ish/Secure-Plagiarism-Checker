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
lis.sort()
    
print(lis[-2])

n = input()
nlist = input().split()
nlist = list(map(int, nlist))
largest = nlist[0]
secLargest = None
for i in range(len(nlist)):
    if nlist[i] > largest:
        temp = largest
        largest = nlist[i]
        secLargest = temp
    elif nlist[i] < largest:
        if secLargest == None:
            secLargest = nlist[i]
        elif nlist[i] > secLargest:
            secLargest = nlist[i]
    
print(secLargest)

dummy = int(input())
a=list(map(int, input().split(" ")))
maxNum=max(a)
count=0
for i in a:
    if i==maxNum:
        count+=1
for i in range(count):
    a.remove(maxNum)
print(max(a))

    

n=int(input())
a=[]
a=input().split()
c=[]
for i in range(0,n):
    c.append(int(a[i]))
c.sort()
z=c.count(c[n-1])
print(c[n-z-1])


input()
print(sorted(list(set(map(int,input().rstrip().split(' ')))))[-2])

N=int(input())
l=[int(i) for i in input().split(" ")]
l.sort(reverse=True)
for i in l:
    if(i!=l[0]):
        print(i)
        break
       
    


N = int(input())
ar = set(map(int, input().split(" ")))
m = max(ar)
while m in ar:
  ar.remove(m)
print(max(ar))

input()
lista = list(set(map(int, input().split())))
print(sorted(lista,reverse=True)[1])


n = input().strip()
a = set(map(int, [x for x in input().strip().split(' ')]))
print(sorted(list(a))[-2])

from heapq import nlargest

N = int(input())
A = {int(a) for a in input().split()}
result = nlargest(2, A)[1]
print(result)

n = int(input())
l = list(map(int, input().split(' ')))
l2 = list(l)
m1 = -1000
while len(l) > 0:
    new = l.pop()
    if new > m1:
        m1 = new
m2 = -1000
while len(l2) > 0:
    new = l2.pop()
    if new > m2 and new != m1:
        m2 = new
print(m2)
            
            

from sys import stdin
data = stdin.read().strip().split()[1:]

nums = list(map(int, data))
nums.sort(reverse=True)
big = nums[0]

for n in nums[1:]:
	if n != big:
		print(n)
		break



input()
print(sorted(set(map(int, input().split(" "))))[-2])

n = int(input())
l = (int(x) for x in input().split(' '))

largest = -101
second_largest = -101
for num in l:
    if num > largest:
        second_largest, largest = largest, num
    elif num > second_largest and num != largest:
        second_largest = num

print(second_largest)

n = int(input())

lst = sorted(set(map(int, input().split())))
