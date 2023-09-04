n = int(input())
for i in range(0,n):
    print(i**2)
a=int(input())
for i in range(0,a):
    print(i*i)
n = int(input())
i = 0
while i < n:
    print(i**2)
    i+=1
a = int(input())
for i in range(0, a):
    print(pow(i, 2))
import sys
N = int(sys.stdin.readline())
for i in range(0,N):
    sys.stdout.write(str(i**2) + "\n")
N=int(input())
if N in range(1,20):
    for i in range(N):
        print(i**2)
a=int(input())
i=0
while i<a:
    print(i*i)
    i+=1
for i in range(int(input())):
    print(i * i)
n = int(input())
for i in range(0,n):
    print(i**2)
n = int(input())
for i in range(n):
    print(i*i)
num = int(input())
for i in range (0,num):
    print(i*i)
a = input()
for i in range(0,a):
    print(i*i)
n = int(input())
i = 0
while i < n:
    print(i*i)
    i+=1
for i in range(input()):
    print(i*i)
a = int(input())
for x in range(a):
    print(x**2)
a = int(input())
for i in range (0,a):
    print(i*i)
n=int(input())
for i in range(n):
    print(i**2)
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