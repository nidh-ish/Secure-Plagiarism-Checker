class Square(RegularPolygon):
    def __init__(self,l,name = "Square"):
        RegularPolygon.__init__(self,4,l,name)
    RegularPolygon.area
# your code for class EquilateralTriangle -- Q.4(c)
class EquilateralTriangle(RegularPolygon):
	def __init__(self,l,name ="Equilateral Triangle"):
		RegularPolygon.__init__(self,3,l,name)
	RegularPolygon.area
# your code for class Pentagon -- Q.4(d) and Q.4(e)
class Pentagon(RegularPolygon):
    def __init__(self,l,name = "Pentagon"):
        RegularPolygon.__init__(self,5,l,name)
if __name__ == "__main__":
  t1 = EquilateralTriangle(5)
  s1 = Square(5)
#  p1 = Pentagon(5)
  print("t1 = ", t1)
  print("s1 = ", s1)
#  print("p1 = ", p1)
class Square(shape):
    def __init__(self,l,name='Square(5)'):
        shape.__init__(self,name)
        self.length=l
    def area(self):
        return (self.length)*(self.length)
    def circumference(self):
        return 4*(self.length)
# your code for class EquilateralTriangle -- Q.4(c)
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
# your code for class Pentagon -- Q.4(d) and Q.4(e)
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
#!/usr/bin/python3
import math
# your code for class Shape  -- Q.4(f)
class Shape():
	def __init__(self,name):
		self.name=name
	def get_details(self):
		return str(self.name)+" (area = "+", circumference = "
# your code for class Triangle -- Q.4(a)
class Triangle(Shape):
	def __init__(self,base,height,name="Triangle"):
		Shape.__init__(self,name)  
		self.base=base
		self.height=height
	def area(self):
		return (0.5)*(self.base)*(self.height)
# code for RegularPolygon is provided below for your use.
class RegularPolygon(Shape):
	def __init__(self, n, l, name="Regular Polygon"):
    		if(n < 3):
      			raise ValueError("Polygons can't have less than 3 sides.")
# your code for class Square -- Q.4(c)
class Square(RegularPolygon):
	def __init__(self,side,name="Square"):
		RegularPolygon.__init__(self,4,side,name)
		self.side=side
# your code for class EquilateralTriangle -- Q.4(c)
class EquilateralTriangle(Triangle):
	def __init__(self,side,name="EquilateralTriangle"):
		Triangle.__init__(self,side,((((3)**(0.5))*(0.5))*(side)),name)
		self.side=side
# your code for class Pentagon -- Q.4(d) and Q.4(e)
class Pentagon(RegularPolygon):
	def __init__(self,side,name="Pentagon"):
		RegularPolygon.__init__(self,5,side,name)
		self.side=side
	def area(self):
		return Square(self.side).area()+EquilateralTriangle(self.side).area()
	def Circumference(self):
		return (4*Square(self.side).get_side())+(3*EquilateralTriangle(self.side).get_side())-2*self.side
if __name__ == "__main__":
  t1 = EquilateralTriangle(5)
  s1 = Square(5)
  p1 = Pentagon(5)

  print("t1 = ", t1)
  print("s1 = ", s1)
  print("p1 = ", p1)

#!/usr/bin/python3
import math
# your code for class Shape  -- Q.4(f)
class Shape:
    def __init__(self,name):
        self.name=name

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