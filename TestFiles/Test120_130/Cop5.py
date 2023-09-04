print(*myList)
from itertools import groupby
seq = input().strip()
for x, y in groupby(seq):
    print((len(list(y)), int(x)), end=" ")
from itertools import groupby
for i,j in groupby(input()):
    print("({0}, {1})".format(len(list(j)),int(i)),sep=' ',end=' ')
    
from itertools import groupby;
s = input().strip();
for key,group in groupby(s,key=None):
    print("("+str(len(list(group)))+", "+str(key)+") ",end="",sep=" ");
import itertools
s = input()
print(" ".join(["({}, {})".format(len(list(g)), k) for k,g in itertools.groupby(s)]))
from itertools import groupby
print(*[(len(list(c)),int(k)) for k,c in groupby(input())])
import itertools as it
s = input()
print(' '.join([ str( (len(list(v)), int(k)) ) for (k, v) in it.groupby(s) ]))

from itertools import groupby
data=input()
for k, g in groupby(data):
    
    print(tuple((len(list(g)),int(k))),end=' ')
#!/usr/bin/env python3
from itertools import groupby
def foo(S):
    groups = []
    for k, g in groupby(S):
        groups.append((k, list(g)))
    for (k,v) in groups:
        print('({}, {}) '.format(len(v), k), end='')
if __name__ == "__main__":
    foo(input())
from itertools import groupby
data=input()
for k, g in groupby(data):
    print((len(list(g)),int(k)),end=" ")
n=int(input())
L=input().split()
l=[int(i) for i in L]
x=[j for i,j in enumerate(l) if j != max(l)]
print(max(x))
from itertools import groupby
from functools import reduce
s = input()
lst = []
for k, v in groupby(s):
    lst.append((len(list(v)), int(k)))
print(reduce(lambda a,b:str(a)+' '+str(b), lst))
s = input() + '/'
curChar = s[0]
curCount = 1
for i in range(1,len(s)):
    if s[i] == curChar:
        curCount += 1
    else:
        print("("+str(curCount)+", "+curChar+")", end = " ")
        curChar = s[i]
        curCount = 1
        
from itertools import groupby
print(*(lambda x: (map(lambda y: (len(y[1]), int((y[0])[0])), map(lambda z: tuple(map(lambda w: tuple(w), z)), x))))(groupby(input().strip())))
from itertools import groupby
chars = input().rstrip()
groups=[]
for k, v in groupby(chars):
    groups.append((len(list(v)), int(k)))
    
print(" ".join(['(%s, %s)' %(k, v) for k, v in groups]))    
chars = input()
from itertools import groupby
lst = [list(g) for k, g in groupby(chars)]
for i in lst:
    print(tuple((len(i),int(i[0]))), end = ' ')
from itertools import groupby
data=input()
for k, g in groupby(data):
    #print(len(list(g)),int(k))
    print ((len(list(g)), int(k)), sep = ", ", end = " ")
from itertools import groupby
s = input().strip()
a = []
for key, count in groupby(s):
    a.append('({}, {})'.format(len(list(count)), key))
print(' '.join(a))

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