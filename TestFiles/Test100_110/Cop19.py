import sys
N = int(input().strip())
if N%2!=0 and N<=100: print('Weird')
if N%2==0 and N>=2 and N<=5 : print ('Not Weird')
if N%2==0 and N>5 and N<=20 : print ('Weird')
if N%2==0 and N>=21 and N<=100: print ('Not Weird')
N = int(input().strip())
if N%2==1:
    print('Weird')
elif N>20:
    print('Not Weird')
elif N>5:
    print('Weird')
elif N>1:
    print('Not Weird')
N = int(input().strip())
res = "Weird"

if N%2 == 0:
    if N<= 5 or N > 20:
        res = "Not Weird"
print(res)
N = int(input().strip())

if(N%2 or 6<=N<=20):
    print("Weird")
else:
    print("Not Weird")
import sys
N = int(input().strip())
if N%2==0:
    if N<6 and N>1:
        print('Not Weird')
    if N>6 and N<21:
        print('Weird')
    if N>20:
        print('Not Weird')
else:
    print('Weird')
N = int(input().strip())
even = (N % 2 == 0)
if(not even or (N >= 6 and N <= 20)):
    print("Weird")
elif(even and ((N >= 2 and N <= 6) or N > 20)):
    print("Not Weird")
N = int(input().strip())
if (N % 2 == 1):
    print("Weird")
elif (N >1 and N <5): 
    print("Not Weird")
elif (N >5 and N <21): 
    print("Weird")
else:
    print("Not Weird")
import sys
N = int(input().strip())
if N%2!=0:
    print ("Weird")
else:
    if N>=2 and N<=5:
        print ("Not Weird")

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