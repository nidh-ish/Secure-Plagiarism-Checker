# else:
if 2<=N and N<=5:
    print('Not Weird')
elif 6<=N and N<=20:
    print('Weird')
elif N > 20:
    print('Not Weird')
#!/bin/python3
import sys
N = int(input().strip())
if N % 2 == 0:
    if N >= 2 and N <= 5:
        print("Not Weird")
    elif N >= 6 and N <= 20:
        print("Weird")
    elif N > 20:
        print("Not Weird")
else:
    print("Weird")
#!/bin/python3
import sys
N = int(input().strip())
if N % 2 == 0:
    if N in range(2,6) or N > 20:
        print('Not Weird')
    else:
        print('Weird')
else:
    print('Weird')    
#!/bin/python3
import sys
N = int(input().strip())
if (N%2 != 0) :
    print("Weird\n")
elif ((N%2 == 0) and (N>=2 and N<=5)) :
    print("Not Weird\n")
elif ((N%2 == 0) and (N>=6 and N<=20)) :
    print("Weird\n")
elif ((N%2 == 0) and (N>20)) :
    print("Not Weird\n")
#!/bin/python3
import sys
N = int(input().strip())
if N%2 != 0:
    print("Weird")
else:
    if N>=2 and N<=5:
        print("Not Weird")
    elif N>=6 and N<=20:
        print("Weird")
    else:
        print("Not Weird")
#!/bin/python
import sys
N = int(input().strip())
if N%2!=0:
    print("Weird")
elif N>=2 and N<=5:
         print("Not Weird")
elif N>=6 and N<=20:
        print("Weird")
else:
    print("Not Weird")
#!/bin/python3
import sys
n = int(input().strip())
if n % 2 == 1:
    print("Weird")
else:
    if n >= 6 and n <= 20:
        print("Weird")
    else:
        print("Not Weird")
#!/bin/python3
import sys
N = int(input().strip())
if(N % 2 != 0):
    print("Weird")
elif(N % 2 == 0 and N in range(2,6)):
    print("Not Weird")
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