for val in range(N):
    print(pow(val,2))
    
N = int(input())
for i in range(0,N):
    print(i**2)
N=int(input())
for i in range(0,N):
    i=i*i
    print(i)

a = int(input())
for i in range(0, a):
    print(i*i)
n = int(input())
for i in range(0,n):
    print(i**2)

n = int(input())
for each in range(n):
    print(each**2)
N = int(input())
i=0
for i in range(0,N):
    print(pow(i,2))
a=int(input())
for i in range(a):
    print(i**2)
a=input()
for x in range(0,a):
	print(x*x)
n = int(input())
for i in range(0,n):
    print(i**2)
for i in range(input()):
    print(i ** 2)
for i in range(int(input())):
    print(i**2)
number = int(input())
for x in range(0,number):
    print(x**2)
raw_integer = int(input())
for i in range(raw_integer):
    print(i**2)
N = int(input())
for i in range(0,N):
    print(pow(i,2))
for i in range(input()):print(pow(i,2))
import sys
d = sys.stdin.readline()
for x in range(0,int(d)):
    print(pow(x,2))
# Python Loops
num = int(input())
for i in list(range(num)):
    print(i**2)
N = int(input())
for i in range(0, N):
    print(i**2)
for i in range(input()):
    print(i*i)
for i in range(int(input())):
    print(pow(i,2))
i = int(input())
for j in range(0, i):
    print(j * j)
n=input()
for i in range(0,n):
    print(i*i)   
i=0
n=int(input())
for i in range(0,n):
    print(i**2)
    i=i+1
a=int(input())
for i in range(0,a):
    print(i**2)
import sys
N = int(sys.stdin.readline())
i = 0
while i<N:
    a = str(pow(i,2))
    sys.stdout.write(a + '\n')
    i = i+1
for i in range(0,int(input())):
    print(i**2)
n = int(input())
for i in range(0,n):
    print(i**2)

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