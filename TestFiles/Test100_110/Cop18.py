a = int(input())
for i in range(0,a):
    print(i**2)
n = int(input())
for x in range(n):
    print(x*x)
n = input()
n = int(n)
i = 0
for i in range(0,n):
    print(i*i)
    i+=1
N = input()
for i in range(0,N):
    print(pow(i,2))
a = int(input())
i = 0
while i < a:
    print(pow(i,2))
    i+=1
a = int(input())
for i in range(0,a):
    print(i**2)
b = int(input())
for i in range(0,b):
    print(i**2)
n= int(input())
for i in range(n):
    print(i**2)
a = int(input(''))
for i in range(a):
  print(i*i)
N = input()
if N>=1 and N<=20:
    for i in range(0,N):
        print(i*i)
n = int(input())
for i in range(n):
    print(i**2)
N=int(input())
for i in range(0,N):
    print(i**2)
a=input()
for i in range(a):
    print(pow(i,2))
a = int(input())
for i in range(0,a):
    print(i**2)
import sys
n = int(input().strip())
if n % 2 == 0:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")
else:
    print("Weird")
N=int(input().strip())

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