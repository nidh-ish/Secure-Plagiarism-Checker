
if (N % 2 == 0 or N > 20) or (N % 2 == 0 and N in range(2, 6)):
    print('Not Weird')
N = int(input().strip());
if N%2!=0 :
    print("Weird");
elif (N>=6 and N<=20) :
    print("Weird");
else :
    print("Not Weird");
N = int(input().strip())
if N % 2 == 1:
    print('Weird')
elif N in range(6, 21):    
    print('Weird')
else:
    print('Not Weird')
N = int(input().strip())
if(N%2 == 0):
    if(N>=2 and N<=5):
        print("Not Weird")
    elif(N>=6 and N<=20):
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")
from itertools import groupby
s = input()
print(*[(len(list(g)), int(k)) for k,g in groupby(s)])
from itertools import groupby
s = input().strip()
res = [(len(list(g)),int(k)) for k,g in groupby(s)]
print(" ".join(map(str, res)))
from itertools import groupby
chars=input()
##chars=sorted(input())
for key,group in groupby(chars):
    print(tuple((len(list(group)),int(key))), end=' ')
from itertools import groupby
S = input()
for c, X in groupby(S):
    print(tuple((len(list(X)), int(c))),end=' ')
import itertools
s = input()
l = [] 
for k, g in itertools.groupby(s):
	t = (k, len(list(g)))
	l.append(t)
s = ""
for t in l:
	s += "(" + str(t[1]) + ", " + t[0] + ") " 
print(s.rstrip())
from itertools import groupby
in_string = input()
groups = []
for g, s in groupby(in_string):
    groups.append((len([x for x in s]), int(g)))
print(*groups, sep=" ")
from itertools import groupby
sample=input()
for x,y in groupby(sample,lambda x: x[0]):
    print ("(%d, %s)"%(len(list(y)),x), end=" ")
input()
l = sorted([int(i) for i in input().split(' ')], reverse=True)
m = l[0]
for i in range(1, len(l)):
    if l[i] < m:
        print(l[i])
        break
import itertools
groups = itertools.groupby(input())
print( " ".join(["(" + str(len(list(k))) + ", " + g + ")" for g, k in groups ]) )
import itertools
data = input()
groups = []
uniquekeys = []
for k, g in itertools.groupby(data):
    groups.append(list(g))      # Store group iterator as a list
    uniquekeys.append(k)
for g, k in zip(groups, uniquekeys):
    print("({0}, {1})".format(len(g), k), end=" ")
from itertools import groupby
print(*[(len(list(c)), int(k)) for k, c in groupby(input())])
from itertools import combinations_with_replacement,combinations,groupby
s = input().strip()
a = [list(g) for k, g in groupby(s)]
for ele in a:
    print('('+str(len(ele))+', '+str(ele[0])+')',end =' ')
from itertools import groupby
print(' '.join([ '({}, {})'.format(len(list(c)), i) for i, c in groupby(input()) ]))
uncompressed = input()

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