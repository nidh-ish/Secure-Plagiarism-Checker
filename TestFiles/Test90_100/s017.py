class Matrix:
  def __init__(self, m):
      self.m = m
    # check if m is empty
      if len(self.m) == 0:
          return MatrixError
    # check if all rows are lists
      for i in self.m:
          if type(i) != list:
              return MatrixError
    # check if all rows are non-empty lists
      for i in self.m:
          if len(i) == 0:
              return MartixError
    # check if all rows are of the same length
      for i in range(len(self.m)):
          for j in range(i+1,len(self.m)):
              if len(self.m[i]) != len(self.m[j]):
                  return MartixError
    # create matrix attribute using deep copy
      self.__matrix__ = deep_copy(m)  
  # method matrix - to return the matrix through deep copy
  def matrix(self):
      return deep_copy(self.m)
  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple
  def dimensions(self):
      a = len(self.m)
      b = len(self.m[0])
      t = (a,b)
      return t     
  # method add - to add two matrices
  def add(self, m):
    # your code here
    l = []
    t1 = dimensions(self.m)
    x = len(m)
    y = len(m[0])
    t2 = (x,y)
    if (t1[0] != t2[0] or t1[1] != t2[1]):
        return MartixError
    for k in range(len(m)):
        for j in range(len(m)):
            l[k][j] = self.m[k][j]+ m[k][j]
    return l            
  # method multiply - to multiply two matrices
  def multiply(self, m):
      l = []
      if len(self.m) != len(m[0]):
          return MartixError
      for i in range(len(self.m)):
          for j in range(len(m[0])):
                  for k in range(len(self.m[0])):
                      l[i][j] = self.m[i][k]*m[k][j]
      return l
  # method transpose - to find the matrix transpose 
  def transpose(self):
    pass
  @static_method
  def deep_copy(m):
      l = []
      for i in m:
          if type(i) == list:
              return deep_copy(i)
          else:
              l.append(i)
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