#!/usr/bin/python3

# MatrixError
# Your code - begin

# Your code - end

class Matrix:
  def __init__(self, m):
    # check if m is empty
    if len(m)==0:
            return None
    # check if all rows are lists
    for i in m:
            if type(i)!=list:
                return None
    # check if all rows are non-empty lists
    for i in m:
            if len(i)==0:
              return None
    # check if all rows are of the same length
    k=len(m[0])
    for i in m:
            if len(i)!=k:
                return None
    # create matrix attribute using deep copy
    self.m=m


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


if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
  print("product1 = ", m1.multiply(m2))
