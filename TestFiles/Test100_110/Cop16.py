i = 0
while i<N:
    a = str(pow(i,2))
    sys.stdout.write(a + '\n')
    i = i+1
for i in range(0,int(input())):
    print(i**2)
n = int(input())
for i in range(0,n):
    print(i**2)
def rdint(n=None):
    if n is None:
        return int(input())
    return [rdint() for _ in range(n)]
n = rdint()
for i in range(n):
    print(i * i)
N = input()
for i in range(N):
    print(i**2)
a=int(input())
for i in range(0,a):
    print(i*i)
a =int(input())
for i in range(0,a):
    print(i**2)
i=int(input())
for n in range(0,i):
    print(pow(n,2))
a=int(input())
i=0
while i<a:
     print(i*i)
     i+=1   
n = int(input())
i = 0
while i<n :
  print(i * i)
  i = i+1
i=input()
for j in range(0,i):
    print(j**2)
n=int(input())
for i in range(0,n):
    print(pow(i,2))
n = int(input())
for i in range(0,n):
    print(i*i)
N = int(input())
for i in range(N):
    print(i**2)
print('\n').join(map(lambda n:n*n,range(input())))
n=int(input())
i=0
while i<n:
    print(i*i)
    i=i+1
n = int(input())

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