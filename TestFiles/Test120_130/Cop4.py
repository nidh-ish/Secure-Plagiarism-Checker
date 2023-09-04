groups = groupby(my_list)
print(" ".join(list("({0}, {1})".format(len(list(v)), k) for k, v in groups)))

from itertools import groupby
a = input()
for key, group in groupby(a):
    print ((len(list(group)), int(key)), end=' ')
from itertools import groupby
print (' '.join([ str((len(list(y)), int(x))) for x, y in groupby(input().strip()) ]))

import itertools
s = input()
for key, group in itertools.groupby(s):
    print((len(list(group)), int(key)), end=" ")
n = int(input())
a = set(map(int,input().split(' ')))
b = list(a)
b.sort()
n = len(b)
print(b[n-2])
from itertools import groupby
s = input().strip()
l = []
for k,g in groupby(s):
    l.append((len(list(g)), int(k)))
print(*l)
import itertools
S = input()
groups=[]
for k,g in itertools.groupby(S):
    groups.append((len(list(g)),int(k)))
print(" ".join([str(g) for g in groups]))
import itertools
s = input()
a = [(len(list(g)),int(k)) for k,g in itertools.groupby(s)]
print(" ".join(map(str,a)))
from itertools import groupby
data = input()
for k, g in groupby(data):
    print(tuple((len(list(g)),int(k))),end=' ')
from itertools import groupby
s = input()
print(*[(len(list(c)), int(k)) for k, c in groupby(s)])
import itertools
s = list(input())
print(" ".join(map(lambda a: str((len(list(a[1])), int(a[0]))), itertools.groupby(s))))
from itertools import *
k = input()
ll = [list(g) for k,g in groupby(k)]
for i in ll:
    qq = (len(i), (int(i[0])))
    print(qq, end=' ')

from itertools import groupby
for i in [(len(list(g)),int(k)) for k, g in groupby(input().strip())]:
    print(i,end=" ")

input_str = input()
output_lst = []
count = 0
prev_elem = ''
for elem in input_str :
    if prev_elem == '' :
        prev_elem = elem
        count += 1
    elif prev_elem != elem : 
        output_lst.append((count,(int)(prev_elem)))
        prev_elem = elem
        count = 1
    else :
        count += 1
output_lst.append((count,(int)(prev_elem)))
        
for elem in output_lst :
    print(elem,end=' ')

from itertools import groupby

def compress(text):
    res = ''
    for key, group in groupby(text, lambda x: x):
        res = res + '({1}, {0})'.format(key, len(list(group))) + ' '
    print(res)

text = input()
compress(text)

N = int(input())
myset = set(int(i) for i in input().strip().split())
print(sorted(myset)[-2])
from itertools import groupby
s = input()
myList = []
for k,g in groupby(s):
    myList.append((len(list(g)),int(k)) )

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
