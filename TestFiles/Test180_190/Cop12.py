class Triangle():
	def __init__(self,b,h):
		self.breadth=b
		self.height=h
	def area(self):
		return (1/2)*self.breadth*self.height
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
		self.num_of_sides=4
		self.length=s
		Shape.__init__(self,name)
class EquilateralTriangle(RegularPolygon):
	def __init__(self,s,name="EquilateralTriangle"):
		self.num_of_sides=3
		self.length=s
		Shape.__init__(self,name)
class  Pentagon(RegularPolygon):
	def __init__(self,s,name="Pentagon"):
		RegularPolygon.__init__(self,5,s,name="Pentagon")
	def area(self):
		return EquilateralTriangle.area(self)+Square.area(self)
if __name__ == "__main__":
  t1 = EquilateralTriangle(5)
  s1 = Square(5)
  p1 = Pentagon(5)
  print("t1 = ", t1)
  print("s1 = ", s1)
  print("p1 = ", p1)
class Shape:
    def __init__(self,name="Shape"):
        self.name = name
    def __str__(self):
        return (self.name+"(area = " + str(self.area()) + ", circumference = " + str(self.circumference()) + ")")
class Triangle(Shape):
    def __init__(self,base,height,name = "Triangle"):
        Shape.__init__(self,name)
        self.b = base
        self.h = height
    def area(self):
        return 0.5 * self.b * self.h
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
    def __init__(self,l,name = "Square"):
        RegularPolygon.__init__(self,4,l,name)
class EquilateralTriangle(RegularPolygon):
    def __init__(self,l,name = "Equilateral Triangle"):
        RegularPolygon.__init__(self,3,l,name)
class Pentagon(RegularPolygon):
    def __init__(self,l,name="Pentagon"):
        RegularPolygon.__init__(self,5,l,name)
        self.square = Square(self.length)
        self.triangle = EquilateralTriangle(self.length)
    def area(self):
        return self.square.area() + self.triangle.area()
if __name__ == "__main__":
  t1 = EquilateralTriangle(5)
  s1 = Square(5)
  p1 = Pentagon(5)
  print("t1 = ", t1)
  print("s1 = ", s1)
  print("p1 = ", p1)
class Shape:
    pass
class Triangle:
    def __init__(self,h,b):
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
    def __init__(self,s,name=" "):
        RegularPolygon.__init__(self,4,s,name)
        self.side=side
    def area(self):
        return RegularPolygon.area(self)
    def circumference(self):
        return RegularPolygon.circumference(self)
    def get_side ():
        pass
class EquilateralTriangle(Triangle):
    Triangle.__init__
if __name__ == "__main__":
  t1 = EquilateralTriangle(5)
  s1 = Square(5)
  p1 = Pentagon(5)
  print("t1 = ", t1)
  print("s1 = ", s1)
  print("p1 = ", p1)

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