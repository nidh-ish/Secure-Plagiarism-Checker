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

num = int(input())
str = input()
numli = []
numli = str.split(' ')
numlist = []
for x in numli:
    numlist.append(int(x))
numlist.sort()
while(numlist[num-1]== numlist[num-2]):
    num = num-1
print(numlist[num-2])

n = input()
a = input().split(' ')
a = [int(i) for i in a]
a = set(a)
a = list(a)
a.sort()
print(a[len(a)-2])


#get input lenght
N = int(input().strip())

#get input
