class Matrix:
  def __init__(self, m):
    # check if m is empty
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
    # your code here
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