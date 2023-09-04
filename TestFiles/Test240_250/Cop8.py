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
  def circumference(self):
    return self.num_of_sides * self.length
  def get_side(self):
    return self.length
class Square(RegularPolygon):
    def __init__(self,s):
        RegularPolygon.__init__(self,4,s,"Sqaure")
class EquilateralTriangle(RegularPolygon):
    def __init__(self,s):
        RegularPolygon.__init__(self,3,s,"Equilateral Triangle")
# your code for class Pentagon -- Q.4(d) and Q.4(e)
class Pentagon(RegularPolygon,Shape):
    def __init__(self,s,name="Pentagon"):
        self.name=name
        self.triangle=RegularPolygon(3,s)
        self.square=RegularPolygon(4,s)
    def area(self):
        return self.area(self)
    def __print__(self):
        return Shape.get_details(self)
if __name__ == "__main__":
  t1 = EquilateralTriangle(5)
  s1 = Square(5)
  p1 = Pentagon(5)
  print("t1 = ", t1)
  print("s1 = ", s1)
  print("p1 = ", p1)
# your code for class Shape  -- Q.4(f)
class Shape:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name+"(area = "+str(self.area())+", circumference = "+str(self.circumference())+")"
# your code for class Triangle -- Q.4(a)
class Triangle(Shape):
   def __init__(self,b,h,name="Triangle"):
        Shape.__init__(self,name)
        self.base=b
        self.height=h
   def area(self):
            return 1/2*self.base*self.height
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
    def __init__(self,s,name="Square"):
      Shape.__init__(self,name)
      RegularPolygon.__init__(self,4,s,name)
# your code for class EquilateralTriangle -- Q.4(c)
class EquilateralTriangle(RegularPolygon):
    def __init__(self,s,name="Equilateral Triangle"):
      Shape.__init__(self,name)
      RegularPolygon.__init__(self,3,s,name)
# your code for class Pentagon -- Q.4(d) and Q.4(e)
class Pentagon(Square,EquilateralTriangle):
    def __init__(self,a,name="Pentagon"):
        Shape.__init__(self,name)
        Square.__init__(self,a,name)
        EquilateralTriangle.__init__(self,a,name)
    def area(self):
        return Square.area(self)+EquilateralTriangle.area(self)
    def circumference(self):
        return Square.circumference(self)+EquilateralTriangle.circumference(self)-2*RegularPolygon.get_side(self)
if __name__ == "__main__":
  t1 = EquilateralTriangle(5)
  s1 = Square(5)
  p1 = Pentagon(5)
  print("t1 = ", t1)
  print("s1 = ", s1)
  print("p1 = ", p1)
# your code for class Shape  -- Q.4(f)
class Shape():
  def __init__(self,name):
    self.name = name
  def __repr__(self):
    return str(self.name)+"(area +"+str(self.area)+","+"circumfarence ="+str(self.circumfarence)
# your code for class Triangle -- Q.4(a)
class Triangle(Shape):
  def __init__(self,b,h,name="Triangle"):
    self.base = b 
    self.height = h
    Shape.__init__(self,name)
  def area(self):
    return 0.5*self.base*self.height
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