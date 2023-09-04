i=int(input())
for n in range(0,i):
    print(pow(n,2))
a=int(input())
i=0
while i<a:
     print(i*i)
     i+=1   
n = int(input())
i = 0
while i<n :
  print(i * i)
  i = i+1
i=input()
for j in range(0,i):
    print(j**2)
n=int(input())
for i in range(0,n):
    print(pow(i,2))
n = int(input())
for i in range(0,n):
    print(i*i)
N = int(input())
for i in range(N):
    print(i**2)
print('\n').join(map(lambda n:n*n,range(input())))
n=int(input())
i=0
while i<n:
    print(i*i)
    i=i+1
n = int(input())
for i in range(n):
    print(i**2)
n = int(input())
for i in range(0,n):
    print(i**2)
a=int(input())
for i in range(0,a):
    print(i*i)
n = int(input())
i = 0
while i < n:
    print(i**2)
    i+=1
a = int(input())
for i in range(0, a):
    print(pow(i, 2))
import sys
N = int(sys.stdin.readline())
for i in range(0,N):
    sys.stdout.write(str(i**2) + "\n")
N=int(input())
if N in range(1,20):
    for i in range(N):
        print(i**2)
a=int(input())
i=0
while i<a:
    print(i*i)
    i+=1
for i in range(int(input())):
    print(i * i)
n = int(input())
for i in range(0,n):
    print(i**2)
n = int(input())
for i in range(n):
    print(i*i)
num = int(input())
for i in range (0,num):
    print(i*i)
    
a = input()
for i in range(0,a):
    print(i*i)
n = int(input())
i = 0
while i < n:
    print(i*i)
    i+=1
for i in range(input()):
    print(i*i)
a = int(input())
for x in range(a):
    print(x**2)
a = int(input())
for i in range (0,a):
    print(i*i)
n=int(input())
for i in range(n):
    print(i**2)
n = int(input())
for i in range(0,n):
    print(i**2)
a = int(input())
for i in range(0,a):
    print(i**2)
n = int(input())
for x in range(n):
    print(x*x)
n = input()
n = int(n)
i = 0
for i in range(0,n):
    print(i*i)
    i+=1
N = input()
for i in range(0,N):
    print(pow(i,2))
a = int(input())
i = 0
while i < a:
    print(pow(i,2))
    i+=1
a = int(input())
for i in range(0,a):
    print(i**2)
b = int(input())
for i in range(0,b):
    print(i**2)
n= int(input())
for i in range(n):
    print(i**2)
a = int(input(''))
for i in range(a):
  print(i*i)
N = input()
if N>=1 and N<=20:
    for i in range(0,N):
        print(i*i)
n = int(input())

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
    