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
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
  print("product1 = ", m1.multiply(m2))
class Matrix:
  def __init__(self, m):
    m_error = Exception("MatrixError: ")
    if(len(m)==0):
        raise m_error
    r_len=[]
    for lsts in m:
        if(type(lsts)!=list or len(lsts)==0):
            raise m_error
        else:
            r_len.append(len(lsts))
    for indices in range(len(m)):
        if r_len[0]!=r_len[indices]:
            raise m_error
    @staticmethod
    def deep_copy(l):
        copied_lst = []
        for elements in l:
            if(type(elements)==list):
                deep_copy(elements)
            else:
                copied_lst.append(elements)
        return copied_lst
    self.m = m
  def matrix(self):
      self.__matrix__ = deep_copy(self.m)
  def dimensions(self):
      return (len(self.__matrix__), len(self.__matrix__[0]))
  def add(self, m):
      ma=[]
      for i in range(len(m)):
          c=[]
          for k in len(m[0]):
              c.append(m[i][k]+self.__matrix__[i][k])
          ma.append(c)
      return str(self.matrix())
if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
  print("product1 = ", m1.multiply(m2))
class MatrixError(Exception):
  def __init__(self):
    Exception.__init__(self)
class Matrix:
  def __init__(self, m):
    if(len(m)==0):
      raise MatrixError()
    for i in m:
      if(type(i)!=list):
        raise MatrixError()
    for i in m:
      if(len(i)==0):
        raise MatrixError()
    x=len(m[0])
    for i in m:
      if(len(i)!=x):
        raise MatrixError
    self.matrix=m[:] 
  def __matrix__(self):
    return self.matrix
  def dimensions(self):
    return (len(self.matrix()),len(self.matrix()[0]))
  def add(self, m):
    l1=[]
    l2=[]
    for i in range(self.matrix()):
      for j in range(self.matrix()[0]):
        l2.append(self.matrix()[i][j]+m.matrix[i][j])
      l1.append(l2)
      l2=[]
    return l1
  @static
  def deep_copy(m):
      return self.matrix()[:]
  def __str__(self):
    return str(self.matrix())
if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
class Matrix:
    def __init__(self, m):
      self.m=m
      self.c=0
      for i in range(len(self.m[i])):
              self.c=self.c+1
      if(len(self.m)==0):
          pass
      for i in range(len(self.m)):
          if(type(self.m[i])!=list):
              break
      for i in range(len(self.m)):
          if(len(self.m[i])==0):
              break
      for i in range(len(self.m)):
          if(len(self.m[i])!=len(self.m[0])):
              break
    @staticmethod
    def deep_copy(l):
        pass

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

    def N(self):
        return self.name
    def P(self):
        return self.parent
    def C(self):
        return self.children

class Family:
 
    p1=Person("A","",("B","C"))
    p2=Person("B","A",("D","E","F"))
    p3=Person("C","A","G")
    p4=Person("D","B","")
    p5=Person("E","B","")
    p6=Person("F","B","")
    p7=Person("G","C","")
    p=[p1,p2,p3,p4,p5,p6,p7]
    def __init__(self):
        self.tree=Family.p
    
    def headOfFamily(self):
     a=0
     for i in range(len(Family.p)):
        if(self.tree[i].P( )==""):
            return self.tree[i].N( )