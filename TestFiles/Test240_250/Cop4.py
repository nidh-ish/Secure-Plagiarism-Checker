for item in result_arr:
    print(item, end=" ")
import itertools
s = list(input())
res = [(sum(1 for i in g), int(k)) for k, g in itertools.groupby(s)]
print(*res)
from itertools import groupby
sample = input()
for key, group in groupby(sample):
    print ((len(list(group)), int(key)), end=' ')
from itertools import groupby
data=input()
for k, g in groupby(data):
    print(tuple((len(list(g)),int(k))),end=' ')
s=input().strip()
from itertools import groupby
res =[]
for k, g in groupby(s):
    res.append('({}, {})'.format(len(list(g)), k))
print(' '.join(res))
import itertools
string = list(input())
lists = []
for key, group in itertools.groupby(string):
    lists.append((len(list(group)), int(key)))
for i in lists:
    print(i, end=" ")
from itertools import groupby
ls = input()
for k, g in groupby(ls, lambda x: x):
    print('({0}, {1})'.format(len([a for a in g]), k), end =' ')
from itertools import groupby
s = input()
S = groupby(s)
print(*[(len(list(y)), (int(x))) for x, y in S])
S = input()
count = 1
last = "a"
for i in S:
    if int(i) == last:
        count += 1
    else:
        if last == 'a':
            last = int(i)
            count = 1
        else:
            print(tuple([count, last]), end = ' ')
            last = int(i)
            count = 1
print(tuple([count, last]))
_ = input()
numbers = set([int(val) for val in input().split()])
print(sorted(numbers)[-2])
from itertools import groupby
string = [int(l) for l in list(input())]
tups = [(len(list(k)),i) for i,k in groupby(string)]
print(*tups,sep=' ')
from itertools import groupby
data = str(input()).strip()
print(*[(int((len(list(j)))),int(i)) for i,j in groupby(data)])
from itertools import groupby
s = input()
gb = groupby(s)
result = ''
for i, j in gb:
    result = result + '(%s, %s) ' % (len(list(j)), i)
result_2 = result.strip()
print(result_2)
import itertools
for i, j in itertools.groupby(input()):
    print(tuple((len(list(j)), int(i))), end = ' ')
from itertools import groupby
a = input()
print(*[(len(list(g)), int(k)) for k, g in groupby(a)])
from itertools import groupby
data = input()
groups = []
uniquekeys = []
for k, g in groupby(data):
    groups.append(list(g))      # Store group iterator as a list
    uniquekeys.append(k)
for i in range(len(groups)):
    a = (len(groups[i]), uniquekeys[i])
    print("({}, {})".format(a[0], a[1]), end=' ')
from itertools import groupby
print(" ".join([str((len(list(g)), int(k))) for k, g in groupby(input().strip())]))
from itertools import groupby
a = input()
for key, group in groupby(a):
    print ((len(list(group)), int(key)), end=' ')
from itertools import *
s = input()
num = [int(k) for k, g in groupby(s)]
num_occ = [len(list(g)) for k, g in groupby(s)]
for i in zip(num_occ, num):
    print(i, end=' ')
input()
A = list(map(int, input().split()))
prev=-1000
cur=A[0]
for i in range(0,len(A)):
    if(A[i]>cur):
        cur=A[i]
for i in range(0,len(A)):
    if(A[i]>prev and A[i]<cur):
        prev=A[i]
print (prev)
num_elements = int(input().strip())
elements = list(set(map(int, (input().split()))))
elements.remove(max(elements))
second_largest = elements.pop(elements.index(max(elements)))
print(second_largest)
n = int(input())
arr = list(map(int,input().split()))
max = -100
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
    def circumference(self):
        return RegularPolygon.circumference
# your code for class Pentagon -- Q.4(d) and Q.4(e)
class Pentagon(Triangle,Square):
    def __init__(self,n,s,name="Pentagon"):
        Square.__init__(self,n,s,name)
        Triangle.__init__(self,n,s,(sqrt(3)/2)*s,name)
        RegularPolygon.__init__(self,n,s,name)
        self.s = s