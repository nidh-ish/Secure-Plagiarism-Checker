#!/usr/bin/python3

# MatrixError
# Your code - begin
# Your code - end

class Matrix:
  def __init__(self, m):
    # check if m is empty
    if(len(m)==0):
      return True
    # check if all rows are lists
    for i in m:
      if(type(i)==list):
        pass
      else:
        return False
    return True
    # check if all rows are non-empty lists
    for i in m:
      if(len(i)>0):
        pass
      else:
        return False
    return True
    # check if all rows are of the same length
    
    # create matrix attribute using deep cop

if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
  print("product1 = ", m1.multiply(m2))