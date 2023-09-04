class Square(RegularPolygon):
    def __init__(self, s, name="Square"):
        RegularPolygon.__init__(self, 4, s, name)
class EquilateralTriangle(RegularPolygon):
    def __init__(self, t, name="EquilateralTriangle"):
        RegularPolygon.__init__(self, 3, t, name)
if __name__ == "__main__":
  t1 = EquilateralTriangle(5)
  s1 = Square(5)
  p1 = Pentagon(5)
  print("t1 = ", t1)
  print("s1 = ", s1)
  print("p1 = ", p1)
class Shape:
	def __init__(self,n):
		self.name=n
	def getdetail(self):
		return self.name+" (area = "+str(self.area())+", circumference = "+str(self.circumference())+" )"
# your code for class Triangle -- Q.4(a)
class Triangle(Shape):
	def __init__(self,breadth,height,name="triange"):
		Shape.__init__(self,name)		
		self.b=breadth
		self.h=height
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
# your code for class Square -- Q.4(c)
class Square(RegularPolygon):
	def __init__(self,length):
		RegularPolygon.__init__(self,4,length,"Square")
# your code for class EquilateralTriangle -- Q.4(c)
class EquilateralTriangle(RegularPolygon):
	def __init__(self,length):
		RegularPolygon.__init__(self,3,length,"EquilateralTriangle")
# your code for class Pentagon -- Q.4(d) and Q.4(e)
class Pentagon(RegularPolygon):
	def __init__(self,length):
		RegularPolygon.__init__(self,5,length,"Pentagon")		
		self.triangle=EquilateralTriangle(length)
		self.square=Square(length)
	def area(self):
		return self.triangle.area()+self.square.area()		
if __name__ == "__main__":
  t1 = EquilateralTriangle(5)
  s1 = Square(5)
  p1 = Pentagon(5)
  print("t1 = ", t1)
  print("s1 = ", s1)
  print("p1 = ", p1)
N = int(input().strip())
if (N % 2 == 1 or (N % 2 == 0 and N >= 6 and N <= 20)):
    print("Weird")
else:
    print("Not Weird")
x=int(raw_input())
for i in range(0,x):
    print(i**2)
def minion_game(s):
    l=len(s)
    s=list(s)
    stuart=0
    kevin=0
    for ii in range(l):
        if s[ii]=="A" or s[ii]=="O" or s[ii]=="U" or s[ii]=="I" or s[ii]=="E":
            kevin=kevin+(l-ii)
        else:
            stuart=stuart+(l-ii)
    if kevin>stuart:
        print("Kevin",kevin)
    elif kevin<stuart:
        print("Stuart",stuart)
    elif kevin==stuart:
        print("Draw")
class Person:
    def __init__(self, n, p, c):
        self.name = n
        self.parent = parent 
        self.children = c
    def __str__(self):
        return 'name '
class Family:
    def __init__(self, n):
        self.tree = n
    def headOfFamily(self):
        return self.tree[0]
class Person : 
	def __init__(self, name, parent, children):
		self.name = name
		self.parent = parent
		self.children = children
class Matrix:
    def __init__(self, m):
        if(len(m)==0):
            raise MatrixError
        for i in m:
            if(type(i) != list):
               raise MatrixError
        for i in m:
            if(len(i) == 0):
                raise MatrixError
        s = len(m[0])
        for i in m:
            if(len(i) != s):
                raise MatrixError
        self.__matrix__ = deep_copy(m)
    @staticmethod
    def deep_copy(l):
        pass
    def add(self, m):
        # your code here
        if (len(self.__matrix__) != len(m)):
            raise MatrixError
        if (len(self.__matrix__[0]) != len(m[0])):
            raise MatrixError
        for i in range(len(self.__matrix__)):
            for j in range(len(self.__matrix__[i])):
                self.__matrix__[i][j] += m[i][j]
        return self.__matrix__
    def multiply(self, m):
        return str(self.matrix())
if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])

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