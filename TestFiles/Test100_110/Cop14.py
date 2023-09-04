n = int(input())
for i in range(n):
    print(i**2)
N = int(input())
if N >= 1 & N <= 20:
    i = 0
    while i < N:
        print(i**2)
        i += 1
n = int(input())
for i in range(0,n):
    print(i**2)
x = int(input())
i = 0
while i < x:
    answer = i**2
    print(answer)
    i = i + 1
a = int(input())
for i in range(a):
    print(pow(i,2))
n=int(input(""))
for i in range (0,n):
    print(i**2)
x = input()
for i in range(x):
    print(i**2)
n = int(input())
i = 0
while i < n:
    print(pow(i, 2))
    i = i + 1
for i in range(0,input()):
    print(i*i)
n = int(input())
i = 0
while i < n:
    print(i*i)
    i = i+1
for i in range(0, input()):
    print(i ** 2)
x = int(input())
for i in range(0,x):
    print(i**2)
N = int(input())
for val in range(N):
    print(pow(val,2))
N = int(input())
for i in range(0,N):
    print(i**2)
N=int(input())
for i in range(0,N):
    i=i*i
    print(i)
a = int(input())
for i in range(0, a):
    print(i*i)
n = int(input())
for i in range(0,n):
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