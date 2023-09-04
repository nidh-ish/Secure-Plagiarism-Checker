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
if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
  print("product1 = ", m1.multiply(m2))

class Matrix:
  def __init__(self, m):
    if len(m)==0:
        return "MatrixError"
    for i in m:
        if type(i)!=list:
            return "MatrixError"
    for i in m:
        if len(i)==0:
            return "MatrixError"
    a=len(m[0])
    for i in m:
        if len(i)!=a:
            return "MatrixError"
    self.__matrix__=self.matrix(m)
  def matrix(self,m):
      return Matrix.deep_copy(m)
  
  def dimensions(self,m):
      return(len(m),len(m[0]))
  def add(self, m):
    temp=[]
    for i in range(len(m.__matrix__)):
        temp.append([])
        for j in range(len(m.__matrix__[0])):
            temp[i].append(m.__matrix__[i][j]+self.__matrix__[i][j])
    return temp
  def multiply(self, m):
    # your code here
    temp=[]
    for i in range(len(self.__matrix__)):
        temp.append([])
        for j in range(len(m.__matrix__[0])):
            temp[i].append(0)

    for i in range(len(self.__matrix__)):
        for j in range(len(m.__matrix__[0])):
            for k in range(len(m.__matrix__)):
                temp[i][j]+=(self.__matrix__[i][k]+m.__matrix__[k][j])
    return temp
  @staticmethod
  # your code here to declare this method as static
  def deep_copy(m):
      m1=[]
      for i in m:
          if type(i)==list:
              m1.append(Matrix.deep_copy(i))
          else:
              m1.append(i)
      return m1
    # your code here

  def __str__(self):
    return str(self.matrix())

if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
  print("product1 = ", m1.multiply(m2))

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