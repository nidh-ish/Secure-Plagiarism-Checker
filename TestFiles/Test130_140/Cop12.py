if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
  print("product1 = ", m1.multiply(m2))
  def matrix(self):
        return deep_copy(self.m)
  def dimensions(self):
      a = len(self.m)
      b = len(self.m[0])
      d = (a,b)
      return d
  def add(self, m):
    # your code here
      l=[]
      d1 = dimensions(self.m)
      x = len(m)
      y = len(m[0])
  def multiply(self, m):
    pass

if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
  print("product1 = ", m1.multiply(m2))
class Matrix:
    def __init__(self, m):
        c=0
        for i in m:
            c+=1
            if c==0:
                raise MatrixError("Not valid matrix")
        for i in m:
            if not isinstance(i,list):raise MatrixError("Not valid matrix")
        for i in m:
            p=len(i)
        if p==0: raise MatrixError("Not valid matrix")
        # check if all rows are of the same length
        list=[]
        for i in m:
            p=len(i)
        list.append(p)
        for i in range(0,len(list)-1):
            if(list[i]!=list[i+1]):raise MatrixError("Not valid matrix")
def add(self, m):
# your code here
    sum=list()
    for i in range(len(m)):
        l=[]
        for j in range(len(m[0])):
            l.append(self[i][j]+m[i][j])
        sum.append(l)
    return sum
@staticmethod
def deep_copy(m):
# your code here
    self.m=[]
    for i in m:
        if isinstance(i,int):self.m.append(i)
        else:self.m.append(deep_copy(i))
    return m

def __str__(self):
    return str(self.matrix())

if __name__ == "__main__":
    m1 = Matrix([[1, 2, 3], [3, 4, 5]])
    m2 = Matrix([[10, 20, 30], [30, 40, 50]])
    print("sum1 = ", str(m1.add(m2)))
    print("sum2 = ", str(m2.add(m1)))

class Matrix:
    def __init__(self, m):
      if len(m) ==0:
          raise MatrixError
      else:
            if map( lambda x: type(x)== 'list' , m) != m:
                raise MatrixError
            else:
                if len(filter( lambda x: len(x)>0 , m)) <= 0:
                    raise MatrixError
                else:
                    if map(lambda x: len(x) == len(m[0]) , m) != m:
                        raise MatrixError
                    else:
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