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
compressed = list()
i = 0
count = 1
while i < len(uncompressed):
    if i == len(uncompressed)-1:
        compressed.append((count, int(uncompressed[i])))
        break
    if uncompressed[i] == uncompressed[i+1]:
        count += 1
    else:
        compressed.append((count, int(uncompressed[i])))
        count = 1
    i += 1
for i in compressed:
    print(i, end=" ")
from itertools import groupby
a = input()
for key, group in groupby(a):
    print ((len(list(group)), int(key)), end=' ')
from itertools import groupby
s = input()
for key,group in groupby(s):
    print((len(list(group)),int(key)),end = ' ')
import itertools
string = input()
groups = []
uniquekeys = []
data = list(string)
for k, g in itertools.groupby(data):
    groups.append(list(g))      # Store group iterator as a list
    uniquekeys.append(k)
for i in groups:
    x = tuple([len(i),int(i[0])])
    print(x,end=' ')
print()
from itertools import groupby
res = []
for k, g in groupby(input()):
    res.append((len(list(g)),int(k)))
print(*res)
a = int(input())
s = set([int(x) for x in input().split(" ")])
l = sorted(list(s))
print(l[-2])
import itertools
print(" ".join(["(%d, %s)"%(len(list(g)), k) for k, g in itertools.groupby(input())]))
word = input()
x = (1, int(word[0]))
for i in word[1:]:
    if int(i) == x[1]:
        x = (x[0] + 1, int(i))
    else:
        print (x, end = ' ')
        x = (1, int(i))
print (x, end = ' ')
import itertools
S = input()
if len(S) == 1:
    print ((1,int(S[0])))
else:
    n = 0
    
    for i in range(1,len(S)):
        if S[i] == S[i-1]:
            n += 1
        else:
            print ((n+1,int(S[i-1])), end = ' ')
            n = 0
print ((n+1,int(S[i])))
from itertools import groupby
print(*[(len(list(c)), int(k)) for k, c in groupby(input())]) #RunLengthCoding
from itertools import groupby
s = input()
print(*[(len(list(g)),int(k)) for k, g in groupby(s)])
from itertools import groupby
data = list(int(item) for item in input())
for k, g in groupby(data):
	t = 0
	for n in g:
		t+= 1
	print(tuple([t, k]), end=" ")
from itertools import groupby
S = input()
group = [(len(list(cgen)), int(c)) for c,cgen in groupby(S)]
print(*group, sep=" ")
import itertools
print(*map(lambda x: (len(list(x[1])), int(x[0])) , itertools.groupby(input())), sep=' ')
import itertools
S = str(input())
S = map(int,list(S))
for k,g in itertools.groupby(S):
    print ((len(list(g)),k),end=' ')
    print(elem[0],list(elem[1]))
st = input()
output = ""
ch_current = st[0]
count = 0
for ch in st:
	if ch == ch_current:
		count += 1
	else:
		output += "(" + str(count) + ", " + str(ch_current) + ") "
		count = 1
		ch_current = ch
output += "(" + str(count) + ", " + str(ch_current) + ") "
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
        self.n = n
    def area(self):
        return Triangle.area + Square.area
    def circumference(self):
        return RegularPolygon.circumference
class Person:
    
    def __init__(self,n,p,c):
        self.name=n
        self.parent=p
        self.children=c
    def N(self):
        return self.name
    def P(self):
        return self.parent
    def C(self):
        return self.children
class Family:
 
    p1=Person("A","",("B","C"))
    p2=Person("B","A",("D","E","F"))
    p3=Person("C","A","G")
    p4=Person("D","B","")
    p5=Person("E","B","")
    p6=Person("F","B","")
    p7=Person("G","C","")
    p=[p1,p2,p3,p4,p5,p6,p7]
    def __init__(self):
        self.tree=Family.p
    
    def headOfFamily(self):
     a=0
     for i in range(len(Family.p)):
        if(self.tree[i].P( )==""):
            return self.tree[i].N( )
    
    def allNodes(self): 
        for i in range(len(Family.p)):
            print(self.tree[i].N( ), end=' ')
        print("\n")
    
    def searchNode(self,n):
        for i in range(len(Family.p)):
            if(n==self.tree[i].N()):
                return True
        else:
            return False
    
    def allAncestors(self,n):
        for i in range(len(Family.p)):
            if(n==self.tree[i].N()):
              print(self.tree[i].P())
    def parent(self,n):
        for i in range(len(Family.p)):
            if(n==self.tree[i].N()):
                print(self.tree[i].P())
        
def t1( ):
 t1=Family( )
 print(t1.headOfFamily())
 t1.allNodes( )
 t1.allAncestors("D")
 print(t1.searchNode("H"))
 t1.parent("B")
if __name__=="__main__":
    t1()