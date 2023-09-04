if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
  print("product1 = ", m1.multiply(m2))
#!/usr/bin/python3
import copy
class Matrix:
  def __init__(self, m):
    
    if(m == []):
        raise MatrixError
    for i in m:
        if(type(i) != list):
            raise MatrixError
    for i in m:
        if(i == []):
            raise MatrixError
    length = len(m[0])
    for i in m:
        if(len(i) != length):
            raise MatrixError
    self.rows = len(m)
    self.col = len(m[0])
    self.__matrix__ = Matrix.deep_copy(m)
  @staticmethod
  def deep_copy(m):
    return copy.deepcopy(m)
  def matrix(self):
    return self.__matrix__
  def dimensions(self):
    return (self.rows, self.col)
  # method add - to add two matrices
  def add(self, m):
      ans = copy.deepcopy(m)
      if(self.dimensions() != m.dimensions()):
          raise MatrixError
      for i in range(self.rows):
          for j in range(self.col):
              ans.__matrix__[i][j] += self.__matrix__[i][j]
      return ans
  def multiply(self, m):
    pass
  # method transpose - to find the matrix transpose 
  def transpose(self):
    ans = []
    for i in range(self.col):
        for j in range(self.rows):
            ans[i][j] = self[j][i]
    return ans
  def __str__(self):
    return str(self.matrix())
if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  
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
class Triangle(Shape):
    def __init__(self,b, h, name="Triangle"):
        Shape.__init__(self,name)
        self.base=b
        self.height=h
    
    def area(self):
        return 0.5*self.base*self.height