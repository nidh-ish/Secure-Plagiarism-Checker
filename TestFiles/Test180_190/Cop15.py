class Square(RegularPolygon):
    def __init__(self,l,name="Square"):
        RegularPolygon.__init__(self,4,l,name)
class EquilateralTriangle(RegularPolygon):
    def __init__(self,l,name="Equilateral Triangle"):
        RegularPolygon.__init__(self,3,l,name)
class Pentagon():
    def __init__(self,l,name="Pentagon"):
        Shape.__init__(self,name)
        self.square=Square(l)
        self.triangle=EquilateralTriangle(l)
        self.side=l
    def area(self):
        return self.triangle.area()+self.square.area()
    def circumference(self):
        return self.triangle.circumference()+self.square.circumference()-(2*self.side)
if __name__ == "__main__":
  t1 = EquilateralTriangle(5)
  s1 = Square(5)
  p1 = Pentagon(5)
  print("t1 = ", t1)
  print("s1 = ", s1)
  print("p1 = ", p1)
class Shape:
    def __init__(self,name):
        self.name=name
    print( str(str(self.name)+" (area = "+str((self.name).area)+", circumference = "+str((self.name).area)+")"))
class Triangle(Shape):
    def __init__(self,b,h,name="Triangle"):
        Shape.__init__(self, name)
        self.b=b
        self.h=h
    def area(self):
        return (self.b*self.h)/2
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
    RegularPolygon.area
class EquilateralTriangle(RegularPolygon):
	def __init__(self,l,name ="Equilateral Triangle"):
		RegularPolygon.__init__(self,3,l,name)
	RegularPolygon.area
class Pentagon(RegularPolygon):
    def __init__(self,l,name = "Pentagon"):
        RegularPolygon.__init__(self,5,l,name)
if __name__ == "__main__":
  t1 = EquilateralTriangle(5)
  s1 = Square(5)
  p1 = Pentagon(5)
  print("t1 = ", t1)
  print("s1 = ", s1)
class Square(shape):
    def __init__(self,l,name='Square(5)'):
        shape.__init__(self,name)
        self.length=l
    def area(self):
        return (self.length)*(self.length)
    def circumference(self):
        return 4*(self.length)
class EquilateralTriangle(shape):
    def __init__(self,a,name='EquilateralTriangle(5)'):
        shape.__init__(self,name)
        self.length=a
    def area(self):
        A=((3**0.5)/(4))
        return (A)*(self.length * self.length)
    def circumference(self):
        p=3*(self.length)
        return p
class Polygon(shape):
    def __init__(self,x,name='Polygon(5)'):
        shape.__init__(self,name)
        self.length=x
    def area(self):
        return (self.length * self.length) + (3**0.5/4)*(self.length * self.length)
    def circumfernce(self):
        return 5*(self.length)
if __name__ == "__main__":
  t1 = EquilateralTriangle(5)
  s1 = Square(5)
  p1 = Polygon(5)
 
  print("t1 = ", t1)
  print("s1 = ", s1)
  print("p1 = ", p1)
class Shape():
	def __init__(self,name):
		self.name=name
	def get_details(self):
		return str(self.name)+" (area = "+", circumference = "
class Triangle(Shape):
	def __init__(self,base,height,name="Triangle"):
		Shape.__init__(self,name)  
		self.base=base
		self.height=height
	def area(self):
		return (0.5)*(self.base)*(self.height)
class RegularPolygon(Shape):
	def __init__(self, n, l, name="Regular Polygon"):
    		if(n < 3):
      			raise ValueError("Polygons can't have less than 3 sides.")
class Square(RegularPolygon):
	def __init__(self,side,name="Square"):
		RegularPolygon.__init__(self,4,side,name)
		self.side=side
class EquilateralTriangle(Triangle):
	def __init__(self,side,name="EquilateralTriangle"):
		Triangle.__init__(self,side,((((3)**(0.5))*(0.5))*(side)),name)
		self.side=side

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