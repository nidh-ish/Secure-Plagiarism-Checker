#!/usr/bin/python3
class MatrixError(Exception):
  def __init__(self, m):
    Exception.__init__(self, m)
class Matrix:
  def __init__(self, m):
    if(len(m) == 0):
      raise(MatrixError("empty matrix"))
    for row in m:
      if(type(row) != list):
        raise(MatrixError("non-list row"))
    for row in m:
      if(len(row) == 0):
        raise(MatrixError("empty row"))
    row_len = len(m[0])
    for row in m:
      if(len(row) != row_len):
        raise(MatrixError("unequal rows"))
    self.__matrix__ = Matrix.deep_copy(m)
  def matrix(self):
    return Matrix.deep_copy(self.__matrix__)
  def dimensions(self):
    num_rows = len(self.__matrix__)
    num_cols = len(self.__matrix__[0])
    return (num_rows, num_cols)
  def add(self, m):
    def add_lists(l1, l2):
      z = zip(l1, l2)
      return [a + b for a, b in z]
    if(self.dimensions() != m.dimensions()):
      raise(MatrixError("add failed: incompatible dimensions"))
    array = m.matrix()
    zipped_rows = zip(self.__matrix__, array)
    return Matrix([add_lists(r1, r2) for (r1, r2) in zipped_rows])
      
  def multiply(self, m):
    def sop(l1, l2):
      return sum([a * b for a, b in zip(l1, l2)])
    _, c1 = self.dimensions()
    r2, c2 = m.dimensions()
    if(c1 != r2):
      raise(MatrixError("multiply failed: incompatible dimensions " + str(self.dimensions()) + ", " + str(m.dimensions())))
    array = m.matrix()
    newm = []
    for row1 in self.__matrix__:
      newrow = []
      for c in range(c2):
        col2 = [r[c] for r in array]
        newrow.append(sop(row1, col2))
      newm.append(newrow)
    return Matrix(newm)
  
  def transpose(self):
    def get_col(i):
      return [row[i] for row in self.__matrix__]
    _, cols = self.dimensions()
    return Matrix([get_col(i) for i in range(cols)])
  @staticmethod
  def deep_copy(m):
    newm = []
    for e in m:
      if(type(e) == list):
        newm.append(Matrix.deep_copy(e))
      else:
        newm.append(e)
    return newm
  def __str__(self):
    return str(self.__matrix__)
def t1():
  try:
    m = Matrix([])
  except MatrixError as e:
    print(e)
def t2():
  try:
    m = Matrix([[1, 2], 2])
  except MatrixError as e:
    print(e)
  
def t3():
  try:
    m = Matrix([[1, 2], []])
  except MatrixError as e:
    print(e)
  
def t4():
  try:
    m = Matrix([[1, 2], [1]])
  except MatrixError as e:
    print(e)
def t5():
  l = [[1, 2], [3, 4]]
  m = Matrix(l)
  l[1][1] = 40
  print("l = ", l)
  print("m = ", m)
  
def t6():
  l = [[1, 2, 3], [3, 4, 5]]
  m = Matrix(l)
  print("dimensions = ", m.dimensions())
def t7():
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
def t8():
  m1 = Matrix([[1, 2, 3], [4, 5, 6]])
  m2 = Matrix([[7, 10, 13], [8, 11, 14], [9, 12, 15]])
  print("product1 = ", m1.multiply(m2))
def t9():
  try:
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[10, 20, 30], [30, 40, 50]])
    print("sum1 = ", str(m1.add(m2)))
  except MatrixError as e:
    print(e)
def t10():
  try:
    m1 = Matrix([[1, 2, 3], [4, 5, 6]])
    m2 = Matrix([[7, 10, 13], [8, 11, 14]])
    print("product1 = ", m1.multiply(m2))
  except MatrixError as e:
    print(e)
def t11():
  try:
    m2 = Matrix([[7, 10, 13], [8, 11, 14]])
    print("transpose = ", m2.transpose())
  except MatrixError as e:
    print(e)
if __name__ == "__main__":
  t1()
  t2()
  t3()
  t4()
  t5()
  t6()
  t7()
  t8()
  t9()
  t10()
  t11()

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
