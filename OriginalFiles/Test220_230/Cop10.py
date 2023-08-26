print(lst[-2])

n=int(input())
a=list(map(int,input().split()))
a.sort()
for i in range(-1,-len(a),-1):
    if(a[i]!=a[i-1]):
        print(a[i-1])
        break

N = int(input())
L = list(map(int, input().split()))
maxL = max(L)
while True:
    try:
        L.remove(maxL)
    except:
        break

print(max(L))

input()
a = [int(n) for n in input().split()]
b = max(a)
while b in a:
    a.remove(b)
print(max(a))

N = int(input())
A = list(map(int, input().split()))
result = []
while A:
    m = max(A)
    if m not in result:
        result.append(m)
    A.remove(m)
print(result[1])

a = int(input())

if( a <=10 and a>=2):
    temp = input()
   
lis = temp.split()
newlist = list(map(int,lis))
newlist.sort()
max = newlist[len(newlist)-1]
if(max <=100 and newlist[0]>=-100):
    max2=max
    i = len(newlist)-1
    while(max2 == max):
        i=i-1
        max2= newlist[i] 
print(max2)        
        

n = input()
L = list(map(int,set(input().split(' '))))
L= sorted(L,reverse=True)
print(L[1])

n = int(input())
numb = input()
lis = list(map(int, numb.split()))
big, sbig = -6000, -6000
for i in lis:
    if (i > big):
        big, sbig = i, big
    elif (i < big and i > sbig):
        sbig = i
print (sbig)

n = int(input())
numbers = list(map(int,input().split()))
numbers.sort()
if numbers.count(max(numbers))== 1:
    second = numbers[-2]
else:
    for i in range(numbers.count(max(numbers))):
        numbers.remove(max(numbers))
    second = numbers[-1]
print(second)


n = int(input())
l = list(map(int, input().split()))
l.sort(reverse=True)
ans = l[0]
for i in range(1, n):
    if l[i] != ans:
        ans = l[i]
        break
print(ans)

n = input()
a = input()
ls = list(map(int, a.split()))
maximum = max(ls)
count = ls.count(maximum)
for i in range (0,count):
    ls.remove(maximum)
print(max(ls))


n = input()

mylist = input()

mylist = list(map(int,mylist.split()))

mylist = sorted(list(set(mylist)))

print(mylist[-2])

i = int(input())
lis = list(map(int,input().strip().split()))[:i]
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print (max(lis))

N = int(input())
lst = list(map(int,input().split()))
firstlargest = max(lst)
a = list()
for i in range(len(lst)):
    if(lst[i]!=firstlargest):
        a.append(lst[i])
secondlargest = max(a) 
print(secondlargest)
    


N=int(input())
temp=0
LargeNos=list(map(int,input().strip().split(' ')))[:N]
x=max(LargeNos)
while max(LargeNos)==x:
        LargeNos.remove(x)
y=max(LargeNos)
print(y)

  
        



n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

arr = [x for x in arr if x!= max(arr)]
print (max(arr))

N = int(input())

lis = list(map(int, input().split()))[:N]
z = max(lis)
while max(lis) == z:
	lis.remove(max(lis))

print(max(lis))


n=int(input())
str=list(map(int,input().split(sep=' ')))
maxi=max(str)
while max(str)==maxi :
    str.remove(maxi)
print (max(str))

input()
s=list(set([int(i) for i in input().split(' ')]))
s.sort()
print(s[-2])

input()
print(sorted(set([int(x) for x in input().split()]))[-2])


n = int(input())
arr = sorted(list(map(int, input().split(' '))), reverse=True)

p = arr[0]
for x in arr:
    if x != p:
        print(x)
        break
    p = x
    
    

n=int(input())
y=input()
lis=[]
lis=list(map(int,y.split()))
large=lis[0]
large2=-100000
for i in range(1,n):
    if(lis[i]>large):
        large2=large
        large=lis[i]
    elif(large>lis[i]>large2):
        large2=lis[i]
print(large2)

int(input())
a =list(map(int,input().split()))
m = max(a)
while max(a)==m:
    a.remove(max(a))
print(max(a))

 




N=int(input())
a=sorted(list(set(int(x) for x in input().strip().split())), key=int)
print(a[len(a)-2])
