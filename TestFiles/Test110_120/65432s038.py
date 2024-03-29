import math
class Shape:
	def __init__(self, name):
		self.name = name

	def get_details(self):
		return self.name + "("  + \
		"area = " + str(self.area()) + \
		", circumference = " + str(self.circumference()) + ")"

class Rectangle(Shape):
	def __init__(self, l, b, name="Rectangle"):
		Shape.__init__(self, name)
		self.length = l
		self.breadth = b

	def area(self):
		return self.length * self.breadth

	def circumference(self):
		return 2 * (self.length + self.breadth)

class Triangle(Shape):
	def __init__(self, b, h, name="Triangle"):
		Shape.__init__(self, name)
		self.base = b
		self.height = h
		self.circumference = 3*b

	def area(self):
		return (1/2)*(self.base)*(self.height)
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
class Square(Rectangle):
	def __init__(self, s, name="Square"):
		Rectangle.__init__(self, s, s, name)

	def get_side(self):
		return self.length

class EquilateralTriangle(Triangle):
	def __init__(self, b, name="EquilateralTriangle"):
		Triangle.__init__(self, b, (math.sqrt(3)*b)/2, name)		

	def area(self):
		return Triangle.area(self)

	def get_details(self):
		return self.name + "("  + \
		"area = " + str(self.area()) + \
		", circumference = " + str(self.circumference) + ")"

class Pentagon(Shape):
	def __init__(self, l, name="Pentagon"):
		Shape.__init__(self, name)
		self.circumference = 5*l
		Square.__init__(self, l, name)
		Triangle.__init__(self, l, (math.sqrt(3)*l)/2, name)
	
	def area(self):
		return Square.area(self)+Triangle.area(self)

	def get_details(self):
		return self.name + "("  + \
		"area = " + str(self.area()) + \
		", circumference = " + str(self.circumference) + ")"

if __name__ == "__main__":
  t1 = EquilateralTriangle(5)
  s1 = Square(5)
  p1 = Pentagon(5)

  print("t1 = ", t1)
  print("s1 = ", s1)
  print("p1 = ", p1)

class Family(Person):

    family_tree = {}
    def __init__(self):
        return
    def headOfFamily(self, nameOfHead):
        self.family_tree[nameOfHead] = []

    def allNodes(self):
        for key in self.family_tree:
            print(key)

    def searchNode(self,n):
        for key in self.family_tree:
            if( key == n):
                return True
        return False
