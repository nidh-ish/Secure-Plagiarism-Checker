class Matrix:
	def __init__(self, m):
		self.m = m
	def empty(self):
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
