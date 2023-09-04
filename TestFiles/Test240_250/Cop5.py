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
# your code for class Square -- Q.4(c)
class Square(RegularPolygon):
    def __init__(self, n,s, name="Square"):
        RegularPolygon.__init__(self,n,s,name)
        self.s = s
        self.n = n
    def area(self):
        return RegularPolygon.area
    def circumference(self):
        return RegularPolygon.circumference
# your code for class EquilateralTriangle -- Q.4(c)
class EquilateralTriangle(RegularPolygon):
    def __init__(self, n,l, name="EquilateralTriangel"):
        RegularPolygon.__init__(self,n,l,name)
        self.l = l
        self.n = n
        self.n = 3
    def area(self):
        return RegularPolygon.area