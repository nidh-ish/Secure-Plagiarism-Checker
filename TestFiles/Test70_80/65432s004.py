import math
# your code for class Shape  -- Q.4(f)
class Shape:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return str(self.name) + "("+\
                "area = " + str(self.area()) +" , " +\
                "circumference = " + str(self.circumference()) + ")"
# your code for class Triangle -- Q.4(a)
class Triangle(Shape):
    def __init__(self,b,h,name = "Triangle"):
        Shape.__init__(self,name)
        self.b = b
        self.h = h

    def area(self):
        return (b*h)/2
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
    def __init__(self,s,name = "Square"):
        RegularPolygon.__init__(self,4,s,name)
# your code for class EquilateralTriangle -- Q.4(c)
class EquilateralTriangle(RegularPolygon):
    def __init__(self,s,name = "Equilateral Triangle"):
        RegularPolygon.__init__(self,3,s,name)
# your code for class Pentagon -- Q.4(d) and Q.4(e)
class Pentagon(RegularPolygon):
    def __init__(self,l,name = "Pentagon"):
        RegularPolygon.__init__(self,5,l,name)
        self.triangle = EquilateralTriangle(l)
        self.s = Square(l)
    def area(self):
        return self.triangle.area() + self.s.area()
    def circumference(self):
        return self.triangle.circumference() + self.s.circumference() - 2*self.triangle.get_side()

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