class MatrixError(Exception):
    def __init__(self,m):
        self.message=m
# Your code - begin
class Matrix:
    def __init__(self,l):
        k=len(l[0])
        if not(len(l)==0):
            for i in l:
                if len(i)!=k or type(i)!='list':
                    raise MatrixError("Error Creating Matrix")
        self.__matrix__=self.deep_copy(l)
    def deep_copy(self,l):
        l=[]
        for i in l:
            l.append([])
            for j in i:
                self.l.append(j)
            return l
    def dimensions(self):
        return (len(self.__matrix__),len(self.__matrix__[0]))
    def add(self,other):
        l=[]
        if self.dimensions()==other.dimensions():
            for i in self.__matrix__:
                l.append([])
                for j,k in self.__matrix__[i],self.__matrix__[i]:
                    l[i].append(j+k)
        else:
            raise MatrixError("Dimensions unequal")
    def multiply(self,other):
        if self.dimensions[1]==other.dimensions[0]:
            pass
            
    def transpose(self):
        i=0
        while(i<len(__matrix__)):
            pass

def check_duplicates(A, p):
    if p >= len(A):
        return A[p]
    elif A[p+1] == A[p]:
        i = p-1
        while i >= 0 and A[i] == A[p]:
            i = i - 1
        return A[i]
    else:
        return A[p]

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def random_partition(A, p, r):
    i = randint(p, r)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)

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