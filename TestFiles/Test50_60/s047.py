class Matrix:
  def __init__(self, m):
    if(len(m)==0):
      return True
    for i in m:
      if(type(i)==list):
        pass
      else:
        return False
    return True

if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
  print("product1 = ", m1.multiply(m2))

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

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
  print("product1 = ", m1.multiply(m2))

def circumference(self):
  return self.num_of_sides * self.length

def get_side(self):
    x = A[r]
    i = p - 1