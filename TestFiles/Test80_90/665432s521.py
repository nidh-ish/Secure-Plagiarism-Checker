import math
class Shape:
  def __init__(self,name):
    pass
  def area(self):
    pass
  def circumference(self):
    pass
  def details(self):
    return name+"("+"area = "+(str)(area())+", circumference = "+(str)(circumference())+")"    

class Triangle(Shape):
  def __init__(self,b,h,name="Triangle"):
    Shape.__init_(self,name)
    self.base=b
    self.height=h
  def area(self):
    return 0.5*self.base*self.height
  
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
  def __init__(self,l,name="Square"):
    RegularPolygon.__init__(self,4,l,name)
    self.side=l
# your code for class EquilateralTriangle -- Q.4(c)
class EquilateralTriangle(RegularPolygon):
  def __init__(self,l,name="EquilateralTriangle"):
    RegularPolygon.__init__(self,3,l,name)
    self.side=l

class Pentagon(RegularPolygon):
  def __init__(self,l,name="Pentagon"):
    RegularPolygon.__init__(self,5,l,name)
    self.side=l
    self.triangle=EquilateralTriangle
    self.square=Square

  def area(self):
    return self.triangle.area+self.square.area()
  def circumference(self):
    return self.triangle.circumference+self.square.circumference()

if __name__ == "__main__":
  t1 = EquilateralTriangle(5)
  s1 = Square(5)
  p1 = Pentagon(5)

  print("t1 = ", t1)
  print("s1 = ", s1)
  print("p1 = ", p1)

class RegularPolygon(Shape):
  def __init__(self, n, l, name="Regular Polygon"):
    if(n < 3):
      raise ValueError("Polygons can't have less than 3 sides.")
    Shape.__init__(self, name)
    self.num_of_sides = n
    self.length = l

  def area(self):
    theta = 2 * math.pi / self.num_of_sides