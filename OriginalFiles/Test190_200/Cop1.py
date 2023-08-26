if __name__ == "__main__":
    m1 = Matrix([[1, 2, 3], [3, 4, 5]])
    m2 = Matrix([[10, 20, 30], [30, 40, 50]])
    print("sum1 = ", str(m1.add(m2)))
    print("sum2 = ", str(m2.add(m1)))
    # print("product1 = ", m1.multiply(m2))


#!/usr/bin/python3

# MatrixError
# Your code - begin

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
                       # self. __matrix__ = Matrix. deep_copy(m
    ''' @static
    def deep_copy(lst):
    l=[]
    if type(lst) == list:
        for i in lst:
           l.append( deep_copy(i))
    return l'''

# Your code - end

    # check if all rows are lists

    # check if all rows are non-empty lists

    # check if all rows are of the same length
    
    # create matrix attribute using deep copy

  # method matrix - to return the matrix through deep copy

  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple
    def dimensions(self):
        return (len(self), len(self[0]))
  # method add - to add two matrices 
    '''def add(self, m):
        a = dimensions(self)
        if a != dimensions(self):
            raise MatrixError
        else:
            l = []
            for i in a[0]:
                l . append( [])
            for i in l:'''
                
            

    # your code here
      

if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
  print("product1 = ", m1.multiply(m2))


#!/usr/bin/python3
import copy


# MatrixError
# Your code - begin
# Your code - end


class Matrix:
  def __init__(self, m):
    
    # check if m is empty
    if(m == []):
        raise MatrixError

    # check if all rows are lists
    for i in m:
        if(type(i) != list):
            raise MatrixError

    # check if all rows are non-empty lists
    for i in m:
        if(i == []):
            raise MatrixError
    
    # check if all rows are of the same length
    length = len(m[0])
    for i in m:
        if(len(i) != length):
            raise MatrixError

    self.rows = len(m)
    self.col = len(m[0])

    # create matrix attribute using deep copy
    self.__matrix__ = Matrix.deep_copy(m)

  # method matrix - to return the matrix through deep copy
  @staticmethod
  def deep_copy(m):
    return copy.deepcopy(m)

  def matrix(self):
    return self.__matrix__

  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple
  def dimensions(self):
    return (self.rows, self.col)

  # method add - to add two matrices
  def add(self, m):
      ans = copy.deepcopy(m)
      if(self.dimensions() != m.dimensions()):
          raise MatrixError
      for i in range(self.rows):
          for j in range(self.col):
              ans.__matrix__[i][j] += self.__matrix__[i][j]
      return ans

  # method multiply - to multiply two matrices
  def multiply(self, m):
    pass

  # method transpose - to find the matrix transpose 
  def transpose(self):
    ans = []
    for i in range(self.col):
        for j in range(self.rows):
            ans[i][j] = self[j][i]
    return ans

  def __str__(self):
    return str(self.matrix())

if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])