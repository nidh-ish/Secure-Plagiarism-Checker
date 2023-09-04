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
    #print(elem[0],list(elem[1]))
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
print(output)
n = input().strip()
m = [int(temp) for temp in input().strip().split()]
for i in range(m.count(max(m))):
    m.remove(max(m))
print(max(m))
from itertools import groupby
s = input()
res = groupby(s)
for char, occ in res:
    print('(%r, %r)' % (len(list(occ)), int(char)), end=" ")
from itertools import groupby
string = input()
def group_counter(s):
    return [(len(list(b)),int(a)) for a,b in groupby(s)] # groups sequential units and counts how many times they occur
print(' '.join(list(map(str,group_counter(string)))))    # -- list(b) is the sequence of the group character ['a', 'a', 'a']

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