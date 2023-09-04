class Matrix:
  def __init__(self, m):
    
    if (len(m)==0):
      raise Exception
    for i in m:
      if (type(i)!='list'):
#        raise Exception
        print("Error")
    for i in m:
      if(len(i)==0):
        raise Exception
    length = len(m[0])
    for i in m:
      if(length!=len(i)):
        raise Exception
    self.m = []
    for i in m:
      self.m.append(m[::])
      
  def matrix(self):
    return self.m

  def dimensions(self):
    self.rows = len(self.m)
    self.columns = len(self.m[0])
    return (self.rows, self.columns)

def add(self, m):
  # your code here
  if (self.dimensions!=m.dimensions):
    print (self.dimensions, m.dimensions)
    raise Exception
  sum = []
  for i in range(1,len(self.m)+1):
    for j in range(1,len(self.m[0])+1):
      sum = self.m[i]+m[i]
  return sum

if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("dim = ", m1.dimensions())

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
  
class Square(RegularPolygon):
    def __init__(self, l, name='Square'):
        RegularPolygon.__init__(self, 4, l, name)

class EquilateralTriangle(RegularPolygon):
    def __init__(self, l, name = "Equilateral Triangle"):
        RegularPolygon.__init__(self, 3, l, name)

class Pentagon(RegularPolygon):
    def __init__(self, l, name = "Pentagon"):
        Shape.__init__(self, name)
        self.length = l
        self.triangle = EquilateralTriangle(self.length)
        self.square = Square(self.length)