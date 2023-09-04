for each in range(n):
    print(each**2)
N = int(input())
i=0
for i in range(0,N):
    print(pow(i,2))
a=int(input())
for i in range(a):
    print(i**2)
a=input()
for x in range(0,a):
	print(x*x)
n = int(input())
for i in range(0,n):
    print(i**2)
for i in range(input()):
    print(i ** 2)
for i in range(int(input())):
    print(i**2)
number = int(input())
for x in range(0,number):
    print(x**2)
raw_integer = int(input())
for i in range(raw_integer):
    print(i**2)
N = int(input())
for i in range(0,N):
    print(pow(i,2))
for i in range(input()):print(pow(i,2))
import sys
d = sys.stdin.readline()
for x in range(0,int(d)):
    print(pow(x,2))
# Python Loops
num = int(input())
for i in list(range(num)):
    print(i**2)
N = int(input())
for i in range(0, N):
    print(i**2)
for i in range(input()):
    print(i*i)
for i in range(int(input())):
    print(pow(i,2))
i = int(input())
for j in range(0, i):
    print(j * j)
n=input()
for i in range(0,n):
    print(i*i)   
i=0
n=int(input())
for i in range(0,n):
    print(i**2)
    i=i+1
a=int(input())
for i in range(0,a):
    print(i**2)
import sys
N = int(sys.stdin.readline())
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