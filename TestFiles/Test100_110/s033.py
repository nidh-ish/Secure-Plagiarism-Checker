class Matrix:
  def __init__(self, m):
        if m == [] or type(m) != type([]):
            raise MatrixError
        for i in m:
            if type(m) != type([]):
                raise MatrixError
            if i == []:
                raise MatrixError        
            if len(i) != len(m[0]):
                raise MatrixError
        self.__matrix__ = deep_copy(m)
  def matrix(self):
     return deep_copy(self.__matrix__)
  def dimensions(self):
        return (len(self.__matrix__),len(self.__matrix__[0]))
  def add(self, m):
      summat = []
      rowsum = []
      for i,j in self.__matrix__, m:
          rowsum = []
          for k,l in i,j:
              rowsum.append(k+l)
              summat.append(rowsum)
  def multiply(self, m):
      pass
  def transpose(self):
    i=0
    j=0
    transpose = []
    for i in range(0,len(self.__matrix__[0])):
        temp = []
        for j in range(0,len(self.__matrix__)):
            temp.append(0)
        transpose.append(temp)    
    for i in range(0,len(self.__matrix__)):
        for j in range(0,len(self.__matrix__)):
            transpose[j][i]=self.__matrix__[i][j]
  @staticmethod
  def deep_copy(l):
        copy=[]
        for i in l:
            if type(i) == type([]):
                copy.append(deep_copy(i))
            else:
                copy.append(i)
        return copy
  def deep_copy(m):
      pass
if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))

class Family(Person):

    family_tree = {}
    def __init__(self):
        return
    def headOfFamily(self, nameOfHead):
        self.family_tree[nameOfHead] = []

    def allNodes(self):
        for key in self.family_tree:
            print(key)

    def searchNode(self,n):
        for key in self.family_tree:
            if( key == n):
                return True
        return False

    def allAncestors(self,n):
        for key,value in self.family_tree:
            for i in value:
                if(n == i):
                    print(key)
                    allAncestors(key)

    def parent(n):
        for key,value in self.family_tree:
            for i in value:
                if(n == 1):
                    print(key)
    num = 1
    def depth(self,n):
        num = 1
        def depth2(n):
            for key,value in self.family_tree:
                for i in value:
                    if(n == i):
                        num = num + 1
                        depth2(key)
        return num

    def addToFamily(self, person):
        if(person.parent not in self.family_tree):
            self.family_tree[person.parent] = []
        #add person as child to parent
        if(person.name not in self.family_tree[person.parent]):
            (self.family_tree[person.parent]).append(person.name)
        #add children of parent
        self.family_tree[person.name] = person.child

    def familyTree(self,vertex ):
        print(vertex)