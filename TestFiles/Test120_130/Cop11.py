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

N = int(input().strip())

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
# code for RegularPolygon is provided below for your use.
class RegularPolygon(Shape):
  def __init__(self, n, l, name="Regular Polygon"):
    if(n < 3):
      raise ValueError("Polygons can't have less than 3 sides.")
    Shape.__init__(self, name)
    self.num_of_sides = n
    self.length = l

  def area(self):
    theta = 2 * math.pi / self.num_of_sides
    phi = (self.num_of_sides - 2) * math.pi / (2 * self.num_of_sides)
    b = self.length
    h = (b * math.tan(phi)) / 2
    area_triangle = 0.5 * b * h
    return self.num_of_sides * area_triangle

  def circumference(self):
    return self.num_of_sides * self.length
