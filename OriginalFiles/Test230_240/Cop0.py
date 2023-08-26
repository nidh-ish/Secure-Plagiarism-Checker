class Person:
    def __init__(self, n, p, c):
        self.name = n
        self.parent = parent 
        self.children = c
    def __str__(self):
        return 'name '


class Family:
    def __init__(self, n):
        self.tree = n
    def headOfFamily(self):
        return self.tree[0]
    




class Person : 
	def __init__(self, name, parent, children):
		self.name = name
		self.parent = parent
		self.children = children
	


#!/usr/bin/python3

# MatrixError
# Your code - begin
# Your code - end

class Matrix:
    def __init__(self, m):
    # check if m is empty
        if(len(m)==0):
            raise MatrixError
    
    # check if all rows are lists
        for i in m:
            if(type(i) != list):
               raise MatrixError
    
    # check if all rows are non-empty lists
        for i in m:
            if(len(i) == 0):
                raise MatrixError

    # check if all rows are of the same length
        s = len(m[0])
        for i in m:
            if(len(i) != s):
                raise MatrixError
        
    # create matrix attribute using deep copy
        self.__matrix__ = deep_copy(m)

  # method matrix - to return the matrix through deep copy
    @staticmethod
    def deep_copy(l):
        pass
        
  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple
    # def dimensions(self):
    #     row = len(self.__matrix__)
    #     col =0
    #     for i in self.__matrix__:
    #         col += len(i)
    #     return (row,col)

  # method add - to add two matrices
    def add(self, m):
        # your code here
        if (len(self.__matrix__) != len(m)):
            raise MatrixError
        if (len(self.__matrix__[0]) != len(m[0])):
            raise MatrixError

        for i in range(len(self.__matrix__)):
            for j in range(len(self.__matrix__[i])):
                self.__matrix__[i][j] += m[i][j]
        return self.__matrix__
  # method multiply - to multiply two matrices
    def multiply(self, m):
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
    # check if m is empty
    m_error = Exception("MatrixError: ")
    if(len(m)==0):
        raise m_error
    r_len=[]
    # check if all rows are lists

    # check if all rows are non-empty lists
    for lsts in m:
        if(type(lsts)!=list or len(lsts)==0):
            raise m_error
        else:
            r_len.append(len(lsts))
    # check if all rows are of the same length
    for indices in range(len(m)):
        if r_len[0]!=r_len[indices]:
            raise m_error
    # create matrix attribute using deep copy
    @staticmethod
    def deep_copy(l):
        copied_lst = []
        for elements in l:
            if(type(elements)==list):
                deep_copy(elements)
            else:
                copied_lst.append(elements)
        return copied_lst
    self.m = m


  # method matrix - to return the matrix through deep copy
    def matrix(self):
        self.__matrix__ = deep_copy(self.m)

  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple
    def dimensions(self):
        return (len(self.__matrix__), len(self.__matrix__[0]))

  # method add - to add two matrices
  def add(self, m):
      ma=[]
      for i in range(len(m)):
          c=[]
          for k in len(m[0]):
              c.append(m[i][k]+self.__matrix__[i][k])
          ma.append(c)
    # your code here
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
class MatrixError(Exception):
  def __init__(self):
    Exception.__init__(self)
class Matrix:
  def __init__(self, m):
    # check if m is empty
    if(len(m)==0):
      raise MatrixError()
    # check if all rows are lists
    for i in m:
      if(type(i)!=list):
        raise MatrixError()
    # check if all rows are non-empty lists
    for i in m:
      if(len(i)==0):
        raise MatrixError()
    # check if all rows are of the same length
    x=len(m[0])
    for i in m:
      if(len(i)!=x):
        raise MatrixError
    # create matrix attribute using deep copy
    self.matrix=m[:] 
  # method matrix - to return the matrix through deep copy
  def __matrix__(self):
    return self.matrix
  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple
  def dimensions(self):
    return (len(self.matrix()),len(self.matrix()[0]))

  # method add - to add two matrices
  def add(self, m):
    l1=[]
    l2=[]
    for i in range(self.matrix()):
      for j in range(self.matrix()[0]):
        l2.append(self.matrix()[i][j]+m.matrix[i][j])
      l1.append(l2)
      l2=[]
    return l1
    
      
  # method multiply - to multiply two matrices
  #def multiply(self, m):
    # your code here
 
  # method transpose - to find the matrix transpose 
 # def transpose(self):
    # your code here
    
  # static method to carry out deep copy of lists
  @static
  def deep_copy(m):
      return self.matrix()[:]

  def __str__(self):
    return str(self.matrix())

if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
 # print("product1 = ", m1.multiply(m2))


#!/usr/bin/python3
