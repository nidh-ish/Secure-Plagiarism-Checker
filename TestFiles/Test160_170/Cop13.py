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

  def get_side(self):
    return self.length