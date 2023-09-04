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
    def get_details(self):
        return str(self.name)+"(area = "+str(self.area)+" ,  circumference = "+str(self.circumference)
class Triangle(Shape):
    def __init__(self,b, h, name="Triangle"):
        Shape.__init__(self,name)
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
    def __init__(self,s, name="Square"):
        Shape.__init__(self,name)
        self.side=s
        RegularPolygon.__init__(self, 4, self.side, name)
        Shape.get_details(self)
class EquilateralTriangle(RegularPolygon):
    def __init__(self, s, name="Equilateral Triangle"):
        Shape.__init__(self, name)
        self.side=s
        RegularPolygon.__init__(self,3 , self.side, name)
        Shape.get_details(self)
# your code for class Pentagon -- Q.4(d) and Q.4(e)
class Pentagon(RegularPolygon):
    def __init__(self ,s , name="Polygon"):
        self.side=s
        RegularPolygon.__init__(self, 5,s,name )
        self.triangle=EquilateralTriangle(self.side)
        self.square=Square(self.side)
        Shape.get_details(self)
            
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
        return(self.name + "("+"area = "+ self.area + " , circumference = " + self.circumference)
class Triangle(Shape):
    def __init__(self,base,height,name="Triangle"):
        Shape.__init__(self,name)
        self.base   = base
        self.height = height
    def area(self):
        return ((1/2.0)*(self.base)*(self.height))
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
        self.length = l
class EquilateralTriangle(RegularPolygon):
    def __init__(self,l,name="EquilateralTriangle"):
        RegularPolygon.__init__(self,3,l,name)
        self.length = l
class Pentagon(RegularPolygon):
    def __init__(self,l,name="Pentagon"):
        RegularPolygon.__init__(self,5,l,name)
        self.length =l
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
    def get_details(self):
        return self.name+'(area = '+str(self.area())+', circumference = '+str(self.circumference())+')'
class Triangle(Shape):
    def __init__(self,b,h,name='Triangle'):
        Shape.__init__(self,name)
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