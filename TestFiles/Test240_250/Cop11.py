class Pentagon(RegularPolygon):
    def __init__(self,s,n=5,name="Pentagon"):
         RegularPolygon.__init__(self,n,s,name)
         self.length=s
         self.triangle=EquilateralTriangle(self.length)
         self.square=Square(self.length)
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
    def __str__(self,name):
        return self.name+'(area = '+str(self.area())+', circumference = '+str(self.circumference())+')'
class Triangle(Shape):
    def __init__(self,b,h):
        self.base = b
        self.height = h
    def area(self):
        return (0.5)*(self.base)*(self.height)
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
    def __init__(self,a,name = "Square"):
        self.length = a
        self.num_of_sides = 4
        RegularPolygon.__init__(self,4,a,name)
class EquilateralTriangle(RegularPolygon):
    def __init__(self,a,name = "Equilateral Triangle"):
        self.length = a
        self.num_of_sides = 3
        RegularPolygon.__init__(self,3,a,name)
class Pentagon(RegularPolygon):
    def __init__(self,a,name = "Pentagon"):
        self.num_of_sides = 5
        self.length = a
        RegularPolygon.__init__(self,5,a,name)
        self.triangle = EquilateralTriangle(a)
        self.square = Square(a)
if __name__ == "__main__":
  t1 = EquilateralTriangle(5)
  s1 = Square(5)
  p1 = Pentagon(5)
  print("t1 = ", t1)
  print("s1 = ", s1)
  print("p1 = ", p1)
class Shape:
    def __init__(sellf,area,circumference,name):
        self.area=area
        self.circumference=circumference
        self.name=name
class Triangle(Shape):
    def __init__(self,b,h,name="Triangle"):
        self.b=b
        self.h=h
    def area(self):
        return ((float)(1)/2)*self.l*self.h
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
    def __init__(self,s,name = "Square"):
          RegularPolygon.__init__(self,4,s,name)
class EquilateralTriangle:
    def __init__(self,s,name="Equilateral Triangle"):
          RegularPolygon.__init__(self,3,s,name)
# your code for class Pentagon -- Q.4(d) and Q.4(e)
if __name__ == "__main__":
  t1 = EquilateralTriangle(5)
  s1 = Square(5)
  p1 = Pentagon(5)
  print("t1 = ", t1)
  print("s1 = ", s1)
  print("p1 = ", p1)
class Shape:
	def __init__(self,name="shape"):
		self.name=name
	def __str__(self):
		return self.name + "(area = " + str(self.area()) + ", Circumference = " + str(self.circumference()) +")" 
class Triangle(Shape):
	def __init__(self,b,h,name="Triangle"):
		self.h=h
		self.b=b
	def area(self):
		return 0.5*self.h*self.b
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
class Pentagon(RegularPolygon):
	def __init__(self,s,name="Pentagon"):
		RegularPolygon.__init__(self,5,s,name)
		self.ars=Square(self.length)
		self.art=EquilateralTriangle(self.length)
	def area(self):
		return self.ars.area()+self.art.area()
if __name__ == "__main__":
  t1 = EquilateralTriangle(5)
  s1 = Square(5)
  p1 = Pentagon(5)
  print("t1 = ", t1)
  print("s1 = ", s1)
  print("p1 = ", p1)
# your code for class Shape  -- Q.4(f)
class Shape:
  def __init__(self, name = "Shape"):
    self.name = name
class RegularPolygon(Shape):
  def __init__(self, n, l, name="Regular Polygon"):
    if(n < 3):
      raise ValueError("Polygons can't have less than 3 sides.")
    Shape.__init__(self, name)
    self.num_of_sides = n
    self.length = l

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
  