class Matrix:
  def __init__(self, m):
    if len(m)==0:
        raise MatrixError
    for e in m:
        if(type(e)!=list):
            raise MatrixError
    for e in m:
        if(len(e)==0):
            raise MatrixError
    d=len(m[0])
    for e in m:
        if(len(e)!=d):
            raise MatrixError
    self.__matrix__=Matrix.deep_copy(m)
  def matrix(self):
      return deep_copy(self.__matrix__)
  def dimensions(self,m):
      return (3,3)
  
  def add(self, m):
    if self.dimensions(self.__matrix__)!=self.dimensions(m):
      raise MatrixError
  # method multiply - to multiply two matrices
  def multiply(self, m):
    # your code here
    row=0
    rowm=0
    for e in m:
        row+=1
    for e in self.__matrix__:
        rowm+=1
    if(len(self.__matrix__[0])!=row):
        raise MatrixError
    m=[]
    k=0
    for j in range(rowm):
        for i in range(row):
            l.append(self.__matrix__[j][i]*m[i][k])
        k+=1
        m.append(l)
    return matrix(m) 
  def transpose(self):
    m=[]
    col=len(self.__matrix__[0])
    for i in range(col):
        l=[]
        for e in self.__matrix__:
            l.append(e[i])
        m.append(l)
  def deep_copy(m):
    # your code here
    l = []
    for e in m:
        if type(e)==list:
            return l.append(Matrix.deep_copy(e))
        else:
            l.append(e)
    return l

  def __str__(self):
    return str(self.matrix())

if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
  print("product1 = ", m1.multiply(m2))

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
  