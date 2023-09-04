n = int(input())
lst = sorted(set(map(int, input().split())))
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

class Shape:
    def __init__(self,name):
        self.name = name
    def get_details(self):
        return self.name + "(" + str(self.area) + "," + str(self.circumference) + ")"               
# your code for class Triangle -- Q.4(a)
class Triangle(Shape):
    def __init__(self,n, b, h, name="Triangle"):
        Shape.__init__(self, name)
        self.b = b
        self.h = h
        self.n = n
        self.n = 3
    def area(self):
        return (1/2)*self.b*self.h