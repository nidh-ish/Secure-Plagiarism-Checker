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
  def deep_copy(m):
      m1=[]
      for i in m:
          if type(i)==list:
              m1.append(Matrix.deep_copy(i))
          else:
              m1.append(i)
      return m1
  def __str__(self):
    return str(self.matrix())
if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
  print("product1 = ", m1.multiply(m2))
class Matrix:
  def __init__(self, m):
      try:
          len(m)>0
          for i in range(len(m)):
              type(m[i])==list
          for i in range(len(m)):
              len(m[i])>0
          for i in range(len(m)-1):
              len(m[i])==len(m[i+1])
          self.m=m    
      except:
          return "MatrixError"
  def add(self, m):
      if len(self.m)==len(m):
        for i in range(len(m)):
           if len(self.m[i])== len(m[i]): 
             for i in self.m:
                for j in self.m[i]:
                  sum[i][j]=self.m[i][j]+m[i][j]
             return sum  
  def multiply(self, m):
      if len(self.m) == len(m):
        for i in range(len(m)):
          if(len(self.m[i])==len(m[i])):
              for i in range(len(self.m)):
                  for j in range(len(m)):
                      for k in range(len(self.m[i])):
                          mul[i][k]=self.m[i][j]+m[j][k]
              return mul
          else:
              return "error"
      else:
          return "error"
  @staticmethod
  def deep_copy(m):
      m1 = []
      for i in m:
          if (type(i)==list):
              return m1.append(deep_copy(i))
          else:
              m1.append(e)
  def __str__(self):
    return str(self.matrix())
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
        list=[]

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
    def allNodes(self): 
        for i in range(len(Family.p)):
            print(self.tree[i].N( ), end=' ')