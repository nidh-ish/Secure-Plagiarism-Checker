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
  def multiply(self, m):
    # your code here
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

        c=0
        for i in m:
            c+=1
            if c==0:
                raise MatrixError("Not valid matrix")
        # check if all rows are lists
        for i in m:
            if not isinstance(i,list):raise MatrixError("Not valid matrix")

        # check if all rows are non-empty lists
        for i in m:
            p=len(i)
        if p==0: raise MatrixError("Not valid matrix")
        # check if all rows are of the same length
        list=[]
        for i in m:
            p=len(i)
        list.append(p)
        for i in range(0,len(list)-1):
            if(list[i]!=list[i+1]):raise MatrixError("Not valid matrix")

# create matrix attribute using deep copy


# method matrix - to return the matrix through deep copy


# method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple

# method add - to add two matrices
def add(self, m):
# your code here
    sum=list()
    for i in range(len(m)):
        l=[]
        for j in range(len(m[0])):
            l.append(self[i][j]+m[i][j])
        sum.append(l)
    return sum

# method multiply - to multiply tw

# static method to carry out deep copy of lists
# your code here to declare this method as static
    @staticmethod
    def deep_copy(m):
    # your code here
        self.m=[]
        for i in m:
            if isinstance(i,int):self.m.append(i)
            else:self.m.append(deep_copy(i))
        return m

    def __str__(self):
        return str(self.matrix())

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
    # '''def add(self, m):
    #     a = dimensions(self)
    #     if a != dimensions(self):
    #         raise MatrixError
    #     else:
