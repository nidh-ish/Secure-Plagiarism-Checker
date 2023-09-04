class Matrix:

  def __init__(self, m):
    # check if m is empty
    if len(m)==0:
      raise SyntaxError("List cannot be empty.")
    for i in m:
      if type(i)!='list':
        raise SyntaxError("Rows must be of type list.")
      elif len(i)==0:
        raise SyntaxError("Rows cannot be empty.")
    length=len(m[0])
    for i in m:
      if len(i)!=length:
        raise SyntaxError("All rows must be of same length.")
    self.__matrix__= deep_copy(m)

  def matrix(self):
    return self.__matrix__
  
  def dimensions(self):
    a=len(self.__matrix__)
    b=len(self.__matrix__[0])
    return (a,b)
  
  def add(self, m):
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
if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
  print("product1 = ", m1.multiply(m2))

def check_duplicates(A, p):
    if p >= len(A):
        return A[p]
    elif A[p+1] == A[p]:
        i = p-1
        while i >= 0 and A[i] == A[p]:
            i = i - 1