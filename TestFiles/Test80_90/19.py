class Person():
    def __init__(self, name, parent, children):
        self.name=name
        self.parent=parent
        if(type(children)==list):
            self.children=children
        elif(type(children)==str):
            self.children=[children]
    def addChildren(self, chi):
        self.children=chi
    def addParent(self, par):
        self.parent=par

class Family():
    def __init__(self, head):
        self.head=head

    def headOfFamily(self):
        return self.head

    def allAncestor(self, per, l=[]):
        if(per.parent!="DNE"):
            l.append(per.parent)
            allAncestor(per.parent, l)
        return l
    @staticmethod
    def allchildren(per, l=[]):
        if(per.children!=["DNE"]):
            l.extend(per.children)
            for child in l:
                Family.allchildren(child, l)
        else:
            return l

    def allNodes(self):
        return [self.head] + Family.allchildren(self.head)

    def searchNode(self, per):
        return per in allNodes(per)

    def parent(self, per):
        return per.paren
    
if __name__ == '__main__':

    A=Person("A", None, [])
    B=Person("B", None, [])
    C=Person("C", None, [])
    D=Person("D", None, [])
    E=Person("E", None, [])
    F=Person("F", None, [])
    G=Person("G", None, [])

    A.addParent("DNE")
    A.addChildren([B, C])

    B.addParent(A)
    C.addParent(A)
    B.addChildren([D, E, F])
    C.addChildren([G])

    D.addParent(B)
    E.addParent(B)
    F.addParent(B)
    G.addParent(C)
    D.addChildren("DNE")
    E.addChildren("DNE")
    F.addChildren("DNE")
    G.addChildren("DNE")

f1=Family(A)

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