import math

class Shape:
  def __init__(self, name):
    self.name = name
    return self.name + "("  + "area = " + str(self.area()) + ", circumference = " + str(self.circumference()) + ")"

class Triangle(Shape):
  def __init__(self,b,h, name="Triangle"):
    Shape.__init__(self, name)  
    self.base = b
    self.height = h

  def area(self):
    return (1.0/2.0)*self.base*self.height
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

class Square(RegularPolygon):
  def __init__(self,s,name="Square"):
    RegularPolygon.__init__(self,4,s,name)

class EquilateralTriangle(RegularPolygon):
  def __init__(self,s,name="EquilateralTriangle"):
    RegularPolygon.__init__(self,3,s,name)

  def area(self):
    return RegularPolygon.area(self)

  def circumference(self):
    return 3*self.base

class Pentagon():
  def __init__(self,s,name="Pentagon"):
    Shape.__init__(self,name)
    self.equilateraltriangle=EquilateralTriangle(s)
    self.square = Square(s)

  def area(self):
    return (self.equilateraltriangle.area()+self.square.area())

  def circumference(self):
    return 5*self.square.length

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
    phi = (self.num_of_sides - 2) * math.pi / (2 * self.num_of_sides)
    b = self.length