class Person():
	def __init__(self,name,parent,children = []):
		self.name = name
		self.parent = parent
		self.children = children
	def __str__(self):
		return "Name = " + str(self.name) + " Parent =" + str(self.parent) 
class Family():
	def __init__(self,obj):
		self.lists = []
		self.headOfFamily = []
		self.listOfNodes = []
		self.listOfNames = []
		
		if(obj.parent == ""):
			self.addHod(obj)
		else:
			self.addObj(obj)
	def addObj(self,obj):
		self.lists.append(obj)
	def addHod(self,obj):
		self.lists.append(obj)
		self.headOfFamily.append(obj)
	def allNodes(self):
		for i in self.lists:
			self.listOfNames.append(i.name)
		for i in self.lists:
			if(i.children == [] and i.parent not in self.listOfNodes):
				self.listOfNodes.append(i.name)
				print(i.name)
			else:
				for x in i.children:
					if(x not in self.listOfNames):
						self.listOfNodes.append(x)
						print(x)
	def searchNode(self,n):
		if(n not in self.listOfNodes):
			print("Not Found")
		else:
			print("Found")
	def allAncestors(self,n):
		if(n not in self.listOfNodes):
			print("Not node")
		else:
			self.Ancestors(n)
	def Ancestors(self,n):
		if (n != self.headOfFamily[0].parent):
			for i in self.lists:
				if(i.name == n and len(i.children) == 0):
					print(i.parent)
					self.Ancestors(i.parent)
				else:
					for x in i.children:
						if n == x:
							print(i.parent)
							self.Ancestors(i.parent)
		return 
	def parent(self,n):
		if (n != self.headOfFamily[0].parent):
			for i in self.lists:
				if(i.name == n and len(i.children) == 0):
					print(i.parent)
				else:
					for x in i.children:
						if n == x:
							print(i.name)
							return
		print("wrong input or head")
	def depth(self):
		count = 0
		head = self.headOfFamily[0].name
	
		for i in self.lists:
			if(i.parent == head and i.name not in self.listOfNodes):
				head = i.name
			count += 1
		print(count)
	def prints(self,person,count):
		print(" " * count, end=' ')
		print((person.name))
		count += 1
		
		for i in self.lists:
			if(i.parent == person.name):
				self.prints(i,count)
			else:
				pass
		return
	def pretty(self):
		count = 0
		print((self.lists))
		print((self.headOfFamily[0].name))
		count += 1
		for i in self.lists:
			if(self.headOfFamily[0].name == i.parent):
				self.prints(i,count)
			else:
				pass
	def __str__(self):
		return "tree = " +str(self.lists) + "headOfFamily = " + str(self.headOfFamily)
def t1():
	x1 = Person("B","A",["D","E","F"])
	x3 = Person("C","A",["G"])
	x2 = Person("A","",["B","C"])
	x4 = Person("H","G")
	x5 = Person("M","H",["P","Q"])
	f1 = Family(x2)
	f1.addObj(x1)
	f1.addObj(x3)
	f1.addObj(x4)
	f1.addObj(x5)
	print("allnodes")
	f1.allNodes()
	print("node search")
	f1.searchNode("G")
	print("Ancestors")
	f1.allAncestors("P")
	print("parent")
	f1.parent("C")
	print("depth")
	f1.depth()
def t2():
	s1 = Person("B","A")
	s2 = Person("C","A")
	s3 = Person("A","")
	familyTree = Family(s3)
	familyTree.addObj(s1)
	familyTree.addObj(s2)
	familyTree.pretty()
if __name__ == "__main__":
	t1()
	t2() 

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

  def area(self):
    theta = 2 * math.pi / self.num_of_sides
    phi = (self.num_of_sides - 2) * math.pi / (2 * self.num_of_sides)
    b = self.length
    h = (b * math.tan(phi)) / 2
    area_triangle = 0.5 * b * h
    return self.num_of_sides * area_triangle

  def circumference(self):
    return self.num_of_sides * self.length

  def get_side(self):
    return self.length
# your code for class Square -- Q.4(c)
class Square(RegularPolygon):
    def __init__(self, n,s, name="Square"):
        RegularPolygon.__init__(self,n,s,name)
        self.s = s
        self.n = n
    def area(self):
        return RegularPolygon.area
    def circumference(self):
        return RegularPolygon.circumference
# your code for class EquilateralTriangle -- Q.4(c)
class EquilateralTriangle(RegularPolygon):
    def __init__(self, n,l, name="EquilateralTriangel"):
        RegularPolygon.__init__(self,n,l,name)
        self.l = l
        self.n = n
        self.n = 3
    def area(self):
        return RegularPolygon.area
    def circumference(self):
        return RegularPolygon.circumference
# your code for class Pentagon -- Q.4(d) and Q.4(e)
class Pentagon(Triangle,Square):
    def __init__(self,n,s,name="Pentagon"):
        Square.__init__(self,n,s,name)
        Triangle.__init__(self,n,s,(sqrt(3)/2)*s,name)
        RegularPolygon.__init__(self,n,s,name)
        self.s = s
        self.n = n
    def area(self):
        return Triangle.area + Square.area
    def circumference(self):
        return RegularPolygon.circumference
class Person:
    
    def __init__(self,n,p,c):
        self.name=n
        self.parent=p
        self.children=c

    def N(self):
        return self.name
    def P(self):
        return self.parent
    def C(self):
        return self.children