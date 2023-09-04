class Person:
    def __init__(my,n,p,c):
        my.name=n
        my.parent=p
        my.children=c

class Family:
    def __init__(my,prs):
        my.members.append(prs)
        members=[]
        a=0

    def headOfFamily(my):
        for i in range(len(my.members)):
            if(my.members[i].parent=="None"):
                return my.members[i].name
        return None

    def allNodes(my):
        for i in range(len(my.members)):
            print(my.members[i].name)            #person.name
        return None
    
    def parent(my,prs):
        return prs.parent

    def searchNode(my,prs):
        for i in range(len(my.members)):
            if(my.members[i]==prs):
                return True
        return False

    def familyTree(my):
        for i in my.members:
            if(i.parent=="None"):
                print(i.name)
            elif(len(i.children)==0):
                print("  " + str(i.name))
            else:
                print(" " + str(i.name))

def test1():
	p1=Person('A','None',['B','C'])
	p2=Person('B','A',['D','E','F'])
	p3=Person('C','A',['G'])
	p4=Person('D','B',[])
	p5=Person('E','B',[])
	p6=Person('F','B',[])
	p7=Person('G','C',[])
	f1=Family(p1)
	f1=Family(p2)
	f1=Family(p4)
	f1=Family(p5)	
	f1=Family(p6)
	f1=Family(p3)
	f1=Family(p7)
	print("head =", f1.headOfFamily())
        

if __name__=="__main__":
    test1()

class RegularPolygon(Shape):
  def __init__(self, n, l, name="Regular Polygon"):
    if(n < 3):
      raise ValueError("Polygons can't have less than 3 sides.")
    Shape.__init__(self, name)
    self.num_of_sides = n
    self.length = l

  def area(self):
    theta = 2 * math.pi / self.num_of_sides
    phi = (self.num_of_sides - 2) * math.pi / (2 * self.num_of_sides)
    b = self.length