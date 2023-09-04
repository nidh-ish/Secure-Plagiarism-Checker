import math
class Shape:
    def __init__(self,name):
        self.n=name

    def display(self):
        return (str(self.n)+"(area = "+str(self.area())+", circumference = "+str(self.circumference())+")")

class Triangle(Shape):
    def __init__(self,b,h):
        self.base=b
        self.height=h

    def area(self):
        return 0.5*self.base*self.height

class RegularPolygon(Shape):
  def __init__(self, n, l, name):
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
    def __init__(self, s):
        self.side=s
        RegularPolygon.__init__(self,4,s,name="Square")
        self.display()

# your code for class EquilateralTriangle -- Q.4(c)
def EquilateralTriangle(RegularPolygon):
    def __init__(self,s):
        RegularPolygon.__init__(self,3,s,name="Triangle")

if __name__ == "__main__":
  s1 = Square(5)

  print("s1 = ", s1)

def circumference(self):
  return self.num_of_sides * self.length

def get_side(self):
  return self.length

def partition(A, p, r):
    x = A[r]
    i = p - 1