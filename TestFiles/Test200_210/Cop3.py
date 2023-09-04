import sys
n = int(input().strip())
if n % 2 == 1:
    print('Weird')
else:
    if n in range(2,6):
        print('Not Weird')
    
    elif n in range(6,21):
        print('Weird')
     
    else:
        print('Not Weird')
N = int(input().strip())
if N%2 == 1 or (N>=6 and N <=20):
    print("Weird")
else:
    print("Not Weird")
N = int(input().strip())
if (N % 2) != 0:
    print("Weird")
if (N % 2 == 0 and N >= 2 and N <= 5):
    print("Not Weird")
if (N % 2 == 0 and N >= 6 and N <= 20):
    print("Weird")
if (N % 2 == 0 and N > 20):
    print("Not Weird")
n = int(input().strip())
message = "Weird" if n % 2 != 0  else "Not Weird" if 2 <= n <= 5 else "Weird" if 6 <= n <= 20 else "Not Weird"
print(message)
n = int(input().strip())
if n%2 != 0:
    print ("Weird")
elif n >= 6 and n<=20:
    print ("Weird")
else:
    print ("Not Weird")
N = int(input().strip())
if N%2==1:
    print("Weird")
else:
    if N>=2 and N<=5:
        print("Not Weird")
    elif N>=6 and N<=20:
        print("Weird")
    elif N>=20:
        print("Not Weird")
N = int(input().strip())
if N%2 == 1: print ("Weird") 
else: 
    if N <= 5: print ("Not Weird")
    elif N <= 20: print ("Weird")
    else: print ("Not Weird")
N = int(input().strip())
if N%2==1: print("Weird")
elif N >= 2 and N <= 5: print("Not Weird")
elif N >= 6 and N <= 20: print("Weird")
elif N > 20: print("Not Weird")
N = int(input().strip())
if N % 2 != 0:
    print("Weird")
else:
    if N > 1 and N < 6:
        print("Not Weird")
    elif N > 6 and N < 21:
        print("Weird")
    elif N > 20:
        print("Not Weird")
N = int(input())
if (N%2) != 0:
    print("Weird")
elif (N%2)==0 and N>=2 and N<=5:
    print("Not Weird")
elif (N%2)==0 and N>=6 and N<=20:
    print("Weird")
elif (N%2)==0 and N>20:
    print("Not Weird")
N = int(input().strip())
if N % 2 == 0:
    if N >= 2 and N <= 5 or N > 20:
        print('Not Weird')
    else:
        print('Weird')
else:
    print('Weird')
N = int(input().strip())
if( N % 2 != 0):
    print("Weird")
else:
    if(N > 20 or N in range(2, 6)):
        print("Not Weird")
    else:
        print("Weird")
n = int(input().strip())
if n == 0 or n<0 or n%2 != 0:
    print("Weird")
elif n in range(2,6):
    print("Not Weird")
elif n in range(6,21):
    print("Weird")
elif n>20:
    print("Not Weird")
N = int(input().strip())
if N % 2 != 0 or (N % 2 == 0 and N in range(6, 21)):
    print('Weird')
elif (N % 2 == 0 or N > 20) or (N % 2 == 0 and N in range(2, 6)):
    print('Not Weird')
N = int(input().strip())
if N%2!=0 :
    print("Weird")
elif (N>=6 and N<=20) :
    print("Weird")
else :
    print("Not Weird")

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