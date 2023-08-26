class Matrix:
    def __init__(self, m):
      self.m=m
      self.c=0
      for i in range(len(self.m[i])):
              self.c=self.c+1
    # check if m is empty
      if(len(self.m)==0):
          pass

    # check if all rows are lists
      for i in range(len(self.m)):
          if(type(self.m[i])!=list):
              break
    # check if all rows are non-empty lists
      for i in range(len(self.m)):
          if(len(self.m[i])==0):
              break
    
    # check if all rows are of the same length
      for i in range(len(self.m)):
          if(len(self.m[i])!=len(self.m[0])):
              break
    # create matrix attribute using deep copy
      @staticmethod
      def deep_copy(l):
          pass


if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
  print("product1 = ", m1.multiply(m2))


#!/usr/bin/python3

# MatrixError

# Your code - begin
# Your code - end

class Matrix:
  def __init__(self, m):
    # check if m is empty
    if len(m)==0:
        return "MatrixError"


    # check if all rows are lists
    for i in m:
        if type(i)!=list:
            return "MatrixError"

    # check if all rows are non-empty lists
    for i in m:
        if len(i)==0:
            return "MatrixError"

    # check if all rows are of the same length
    a=len(m[0])
    for i in m:
        if len(i)!=a:
            return "MatrixError"
    # create matrix attribute using deep copy
    self.__matrix__=self.matrix(m)
  # method matrix - to return the matrix through deep copy
  def matrix(self,m):
      return Matrix.deep_copy(m)
  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple
  def dimensions(self,m):
      return(len(m),len(m[0]))
  # method add - to add two matrices
  def add(self, m):
    # your code here
    temp=[]
    for i in range(len(m.__matrix__)):
        temp.append([])
        for j in range(len(m.__matrix__[0])):
            temp[i].append(m.__matrix__[i][j]+self.__matrix__[i][j])
    return temp

  # method multiply - to multiply two matrices
  def multiply(self, m):
    # your code here
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

  # method transpose - to find the matrix transpose
  #def transpose(self):
    # your code here

  # static method to carry out deep copy of lists
  @staticmethod
  # your code here to declare this method as static
  def deep_copy(m):
      m1=[]
      for i in m:
          if type(i)==list:
              m1.append(Matrix.deep_copy(i))
          else:
              m1.append(i)
      return m1
    # your code here

  def __str__(self):
    return str(self.matrix())

if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
  print("product1 = ", m1.multiply(m2))


#!/usr/bin/python3

# MatrixError
# Your code - begin
# Your code - end

class Matrix:
  def __init__(self, m):
      try:
    # check if m is empty
          len(m)>0
    # check if all rows are lists
          for i in range(len(m)):
              type(m[i])==list

    # check if all rows are non-empty lists
          for i in range(len(m)):
              len(m[i])>0

    # check if all rows are of the same length
          for i in range(len(m)-1):
              len(m[i])==len(m[i+1])
          self.m=m    
      except:
          return "MatrixError"
    
    # create matrix attribute using deep copy

  # method matrix - to return the matrix through deep copy

  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple

  # method add - to add two matrices
  def add(self, m):
      if len(self.m)==len(m):
        for i in range(len(m)):
           if len(self.m[i])== len(m[i]): 
             for i in self.m:
                for j in self.m[i]:
                  sum[i][j]=self.m[i][j]+m[i][j]
             return sum  
    # your code here
      
  # method multiply - to multiply two matrices
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
    # your code here
 
  # method transpose - to find the matrix transpose 
#  def transpose(self):
    # your code here
    
  # static method to carry out deep copy of lists
  # your code here to declare this method as static
  @staticmethod
  def deep_copy(m):
      m1 = []
      for i in m:
          if (type(i)==list):
              return m1.append(deep_copy(i))
          else:
              m1.append(e)
    # your code here

  def __str__(self):
    return str(self.matrix())

if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
  print("product1 = ", m1.multiply(m2))


#!/usr/bin/python3
  # method matrix - to return the matrix through deep copy
  def matrix(self):
        return deep_copy(self.m)
  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple
  def dimensions(self):
      a = len(self.m)
      b = len(self.m[0])
      d = (a,b)
      return d
  # method add - to add two matrices
  def add(self, m):
    # your code here
      l=[]
      d1 = dimensions(self.m)
      x = len(m)
      y = len(m[0])
    #   d2 = 
  # method multiply - to multiply two matrices
  # def multiply(self, m):
    # your code here
