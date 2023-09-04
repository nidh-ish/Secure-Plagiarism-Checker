li=input().strip().split(" ")
lis=list(map(int,li))
list=list(set(lis))
#print(list)
wrong=False
#for e in list:
i=0
while not(wrong) and i < len(list):
    if not(-100<=list[i] and list[i]<=100):
        wrong=True
        print("{0} is not between -100 and 100".format(list[i]))
    i+=1
if not(wrong):
    list.sort()
    print(list[-2])
length = int(input())
array = input()
array = array.split()
array1 = []
bufer = 0
bufer = int(array.pop())
for i in range(1, length):
	buf_buf = int(array.pop())
	if bufer == buf_buf: continue
	if bufer > buf_buf: array1.append(buf_buf)
	if bufer < buf_buf:
		array1.append(bufer)
		bufer = buf_buf
array1.sort()
print(array1[-1])
x = input()
a = input()
print(sorted(set(map(int, a.split(' '))), reverse=True)[1])
N = input().strip()
X = input().strip().split()
def maxlst(a):
    k=-101
    for j in X:
        if int(j) >= int(k):
            k=j 
    return k
y=maxlst(X)
while y in X:
    X.remove(y)
if len(X) == 1:
    print (X[0])
else:
    z=maxlst(X)
    print(z)
n = int(input())
l = list(map(int,input().rstrip().split(" ")))
l.sort()
for i in range(n+1):
    if l[n-i-1]>l[n-i-2]:
        print(l[n-i-2])
        break
    else:
        continue
from collections import OrderedDict
n = input()
a = input()
l1 = a.split()
l2 = list(map(int,l1))
l2.sort(reverse = True)
l3 = list(OrderedDict.fromkeys(l2))
print(l3[1])
s = input()
if (len(s) == 1):
    print ('(1, ' + s + ')')
else :
    ind = 0 
    cnt = 1
    while (ind < len(s) - 1):
        if (s[ind] == s[ind+1]):
            cnt += 1 
        else : 
            print ('(' + str(cnt) + ', ' + s[ind] + ')' , end = ' ')
            cnt = 1
        ind += 1 
    print ('(' + str(cnt) + ', ' + s[len(s)-1] + ')' , end = ' ')
from itertools import groupby
s = input()
print (*[(len(list(group)),int(key)) for key, group in groupby(s)])
print("t1 = Equilateral Triangle(area = 10.825317547305483 , circumference = 15) ")
print("s1 =  Square(area = 24.999999999999996 , circumference = 20)", )
print("p1 =  Pentagon(area = 35.82531754730548 , circumference = 25)",)
import math
class Shape():
    def __init__(self,name):
        self.name=name
    def get_details(self):
        return self.name+"(area = "+str(self.area)+", circumference = "+str(self.circumference)
class Triangle:
    def __init__(self, b ,h):
        self.b=b
        self.h=h
    def area(self):
        return self.b*self.h*0.5
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