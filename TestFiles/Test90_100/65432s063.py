import math

class Shape():
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return(self.name + str("(area = ") + str(self.area()) +str(", ")+ str("circumference") + str(" = ") + str(self.circumference()) + str(")") )

class Triangle(Shape):
    def __init__(self,base,height,name = "Triangle"):
        Shape.__init__(self,name)
        self.b = base
        self.h = height

    def area(self):
        return (1.0/2)*self.b*self.h
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
    def __init__(self,side,n=4,name = "Square"):
        RegularPolygon.__init__(self,n,side,name)
        self.l = side

    def circumference(self):
        return 4*self.l
class EquilateralTriangle(RegularPolygon):
    def __init__(self,side,n=3,name = "Equilateral Triangle"):
        RegularPolygon.__init__(self,n,side,name)
        self.l = side

    def circumference(self):
        return 3*self.l

class Pentagon(Square,EquilateralTriangle,RegularPolygon):
    def __init__(self,side,n=5,name = "Pentagon"):
        RegularPolygon.__init__(self,side,n,name)
        self.l = side
        self.triangle = EquilateralTriangle(self.l)
        self.square = Square(self.l)

    def area(self):
        return self.triangle.area()+self.square.area()

    def circumference(self):
        return 5*self.l

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
    h = (b * math.tan(phi)) / 2
    area_triangle = 0.5 * b * h
    return self.num_of_sides * area_triangle

  def circumference(self):
    return self.num_of_sides * self.length