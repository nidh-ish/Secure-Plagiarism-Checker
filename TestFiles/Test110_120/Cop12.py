import sys
n = int(input().strip())
if (n>20):
    if(n%2==0):
        print("Not Weird")
    else:
        print("Weird")        
else:
    if(n%2==0):
        if n in range(2,6):
            print("Not Weird")
        else:
            print("Weird")
    else:
        print("Weird")
#!/bin/python3
import sys
N = int(input().strip())
if (N%2 != 0) | ((N>= 6) & (N <= 20)) :
    print( "Weird")
else:
    print( "Not Weird")
#!/bin/python3
import sys
N = int(input().strip())
if (N%2 != 0): print ("Weird")   
else:
    if(N<=5): print("Not Weird")
    elif(N>5 and N<=20): print("Weird")
    else: print("Not Weird")
N = int(input())
if (N%2!=0) or (N%2==0 and N>=5 and N<=20):
    print ("Weird")
else:
    print ("Not Weird")
#!/bin/python3
import sys
N = int(input().strip())
weird = 'Weird'
not_weird = 'Not Weird'
if N % 2 != 0:
    print(weird)
elif N >= 2 and N <= 5 and N % 2 == 0:
    print(not_weird)
elif N >= 6 and N <= 20 and N % 2 == 0:
    print(weird)
elif N >= 20 and N % 2 == 0:
    print(not_weird)
#!/bin/python3
import sys
N = int(input().strip())
if N%2 != 0:
    print('Weird')
else:
    if N > 1 and N < 6:
        print('Not Weird')
    elif N > 5 and N < 21:
        print('Weird')
    elif N > 20:
        print('Not Weird')
#!/bin/python3
import sys
N = int(input().strip())
if(N % 2 == 1):{
   print("Weird")
    }
elif(N < 6):
    {
    print("Not Weird")
    }
elif(N< 21):
    {
        print ("Weird")
    }
else: print("Not Weird")
#!/bin/python3
import sys
class Shape:
	def __init__(self, name):
		self.name = name
	def get_details(self):
		return self.name + "("  + \
		"area = " + str(self.area()) + \
		", circumference = " + str(self.circumference()) + ")"
class Rectangle(Shape):
	def __init__(self, l, b, name="Rectangle"):
		Shape.__init__(self, name)
		self.length = l
		self.breadth = b
	def area(self):
		return self.length * self.breadth
	def circumference(self):
		return 2 * (self.length + self.breadth)
class Triangle(Shape):
	def __init__(self, b, h, name="Triangle"):
		Shape.__init__(self, name)
		self.base = b
		self.height = h
		self.circumference = 3*b
	def area(self):
		return (1/2)*(self.base)*(self.height)
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