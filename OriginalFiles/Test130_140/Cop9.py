import sys

N = int(input().strip())

if (N % 2 == 1 or (N % 2 == 0 and N >= 6 and N <= 20)):
    print("Weird")
else:
    print("Not Weird")
    


x=int(raw_input())
for i in range(0,x):
    print(i**2)

def minion_game(s):
    l=len(s)
    s=list(s)
    stuart=0
    kevin=0
    for ii in range(l):
        if s[ii]=="A" or s[ii]=="O" or s[ii]=="U" or s[ii]=="I" or s[ii]=="E":
            kevin=kevin+(l-ii)
        else:
            stuart=stuart+(l-ii)
                
    if kevin>stuart:
        print("Kevin",kevin)
    elif kevin<stuart:
        print("Stuart",stuart)
    elif kevin==stuart:
        print("Draw")
              

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

