import sys
class Person:
    def __init__(self,n,p,c):
        self.name=n    #This is a string
        self.parent=p   # This is a string
        self.children=c # This is a string list
    def __str__(self):
        s=""
        for i in self.children:
            s+=i.name
        if self.parent==None:
            return "Name is : " + str(self.name) + "\n Parent Name is : " + "None" + "\n Children Name is : "+ s + "\n"
        else:
            return "Name is : " + str(self.name) + "\n Parent Name is : " + str(self.parent.name) + "\n Children Name is : "+ s + "\n"

class Family:
    def __init__(self,rootnode=Person("A","None",[])):
        self.headOfFamily=rootnode
        self.l=[]
        self.l.append(self.headOfFamily)
    def headoffamily(self):
        print(self.headOfFamily)
    def makechild(self,p,c):
        for i in self.l:
            #print str(i)
            if p.name==i.name:
                i.children.append(c)
                self.l.append(c)
    def allNodes(self):
        for i in self.l:
            print(i)
    def searchNode(self,n):
        for i in self.l:
            if i==n:
                return True
        return False
    def searchNodewithName(seldf,n):
        for i in self.l: 
            if i.name==n:
                return True
        return False    
    def allAncestors(self,n):
        print("The person and his/her ancestors are")
        for i in self.l:
            if n==i:
                an=n
                while an.parent!=None:
                    print(str(an))
                    an=an.parent
                    if an.parent==None:
                        break
                break
    def numancestors(self,q):
        ans=q
        counter=0
        while ans!=None:
            counter+=1
            ans=ans.parent
            #print "ans is ",ans
        return counter-1
    def parent(self,n):
        for i in self.l:
            if i==n:
                if i.parent!=None:
                    print(i.parent.name)
                else:
                    print("None")
    def depth(self):
        ans=self.headOfFamily
        counter=0
        while ans.children!=[]:
            counter+=1
            if ans.children==None:
                break
            else:
                ans=ans.children[0]
        return counter
    def child(self,i,space):
        count=0
        while count<space:
            sys.stdout.write(' ')
            count+=1
        print(i.name)
    def printtree(self):
        def recur(l):
            if l.children!=[]:
                self.child(l,self.numancestors(l))
                for i in l.children:
                    recur(i)
            else:
                self.child(l,self.numancestors(l))
        recur(self.headOfFamily)

print("Creating Objects")
A=Person("A",None,[])
B=Person("B",A,[])
C=Person("C",A,[])
D=Person("D",B,[])
E=Person("E",B,[])
F=Person("F",B,[])
G=Person("G",C,[])
H=Person("H",G,[])
print("Creating Family")
Fa=Family(A)
print("Making Relations")
Fa.makechild(A,B)
Fa.makechild(A,C)
Fa.makechild(B,D)
Fa.makechild(B,E)
Fa.makechild(B,F)
Fa.makechild(C,G)
print("Printing All Nodes")
Fa.allNodes()
print("printing Ancestors")
Fa.allAncestors(B)
Fa.allAncestors(E)
Fa.allAncestors(G)
print("Searching for B and H in Tree")
print(Fa.searchNode(B))
print(Fa.searchNode(H))
print("Parent of B and A")
Fa.parent(B)
Fa.parent(A)
print("Depth Count")
print(Fa.depth())
print("")
print("Number of ancestos of C and G")
print(Fa.numancestors(C))
print(Fa.numancestors(G))
print("")
Fa.printtree()

class Shape:
    def __init__(self,name):
        self.name = name
    def get_details(self):
        return self.name + "(" + str(self.area) + "," + str(self.circumference) + ")"               
# your code for class Triangle -- Q.4(a)
class Triangle(Shape):
    def __init__(self,n, b, h, name="Triangle"):
        Shape.__init__(self, name)
        self.b = b
        self.h = h
        self.n = n
        self.n = 3
    def area(self):
        return (1/2)*self.b*self.h
# code for RegularPolygon is provided below for your use.
class RegularPolygon(Shape):
  def __init__(self, n, l, name="Regular Polygon"):
    if(n < 3):
      raise ValueError("Polygons can't have less than 3 sides.")
    Shape.__init__(self, name)
    self.num_of_sides = n
    self.length = l