#!/usr/bin/python3

# MatrixError
# Your code - begin
# Your code - end

class Matrix:
  def __init__(self, m):
    self.m=m
    # check if m is empty
    k=[]
    for i in range(len(m)):
        for j in range(len(m[0])):
            if(m[i][j]==0):
                k.append(False)
              
    for l in range(len(k)):
        if(k[l]==True):
            continue
        else:
            raise MatrixError("matrix cannot be null")

    # check if all rows are lists
    for i in range(len(m)):
        if(type(m[i]!=list)):
            raise MatrixError("detected non-list row")

    # check if all rows are non-empty lists
    for i in range(len(m)):
        p=[]
        for j in range(len(m[0])):
            if(m[i][j]==0):
                p.append(False)
        for a in range(len(p)):
            if(p[a]==True):
                continue
            else:
                raise MatrixError("Row cannot be null")
    # check if all rows are of the same length
    for i in range(len(m)):
        if(len(m[0])!=len(m[i])):
            raise MatrixError("Unequal length of rows")

    # create matrix attribute using deep copy
   # self.__matrix__=self.deep_copy(m)
   # @staticmethod
   # def deep_copy(se



  # method matrix - to return the matrix through deep copy
  #def matrix(self):
   #   return m
  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple
  def dimensions(self):
      return (len(self.m),len(self.m[0]))
  # method add - to add two matrices
  def add(self, m):
      z=[]
      for i in range(m):
          for j in range(m[0]):
              z.append(0)
      for i in range(m):
          for j in range(m[0]):
              z[i][j]=self.m[i][j]+m[i][j]
          
        
    # your code here

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
if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("product1 = ", m1.multiply(m2))
