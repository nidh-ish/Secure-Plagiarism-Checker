import itertools
S = input()
for a, b in itertools.groupby(S):
    print((len(list(b)), int(a)), end=' ')
from itertools import groupby
S = input()
for x in groupby(S):
    print('(%s, %s)' % (len(list(x[1])), x[0]), end=' ')
from itertools import groupby
nums = [int(i) for i in input()]
print(*[(sum(map(lambda x: 1, g)), k) for k, g in groupby(nums)])
import itertools
a = input()
a = [int(aa) for aa in a]
res = []
for k, v in itertools.groupby(a):
    res.append((len(list(v)), k))
print(' '.join(map(str, res)))
# Compress the String!
from itertools import groupby
s = input().strip()
# print([(int(k), len(list(v))) for (k,v) in list(groupby(s))])
for k, v in groupby(s):
  print((len(list(v)), int(k)), end=" ")

from itertools import groupby as g
s= input()
for i, j in g(s):
    print((len(list(j)), int(i)), end=' ')
import itertools
s = input() 
print(*[(len(list(b)), int(a)) for a,b in itertools.groupby(s)])
from itertools import groupby
S = input()
print(" ".join([str((len(list(g)), int(k))) for k, g in groupby(S)]))
N = int(input())
A = input().split()
A = list(map(int,A))
q = max(A)
while max(A)==q:
    A.remove(max(A))
    
print(max(A))
from itertools import groupby

def RLE(s):
    return [(len(list(g)), k) for k, g in groupby(s)]

def main():
    s = input()
    r = RLE(s)
    for i in r:
        print("({0}, {1})".format(i[0], i[1]), end=" ")
    print()
    
if __name__ == '__main__':
    main()

from itertools import groupby
s = input()
tuples = []
for k, g in groupby(s):
    occs = len(list(g))
    tuples.append((occs, int(k)))
print(' '.join([str(t) for t in tuples]))

from itertools import groupby
print( *[  ( len(list(c)), int(k) ) for k, c in groupby(input())  ] )
from itertools import groupby
data=input()
for k, g in groupby(data):
    print(tuple((len(list(g)),int(k))),end=' ')

from itertools import groupby
S = input().strip()
groups = []
for key, group in groupby(S):
    groups.append((len(list(group)), int(key)))
print(*groups, sep=' ')
from itertools import groupby
stri = list(map(int, input()))
groups = []
uniquekeys = []
for k, g in groupby(stri):
    groups.append(list(g))
    uniquekeys.append(k)
l = [(len(i), j) for i, j in zip(groups, uniquekeys)]
for i in l:
    print(i, end=" ")
from itertools import groupby
my_list = map(int, input())

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
