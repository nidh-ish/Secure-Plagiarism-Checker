if(N % 2 == 0 and N in range(6,21)):
    print("Weird")
elif(N % 2 == 0 and N > 20):
    print("Not Weird")
    
#!/bin/python3
import sys
n = int(input().strip())
if n%2 == 0:
    if n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")
#!/bin/python3
import sys
N = int(input().strip())
if N%2 == 1:
    print("Weird")
elif N >= 2 and N <= 5:
    print("Not Weird")
elif N >= 6 and N <= 20:
    print("Weird")
elif N >= 21:
    print("Not Weird")
#!/bin/python3
import sys
N = int(input().strip())
if N % 2 == 0:
    if 2 <= N <=5:
        print ("Not Weird")
    elif 6<= N <= 20:
        print ("Weird")
    elif N > 20:   
        print ("Not Weird")
else:
    print ("Weird")
#!/bin/python3
import sys
N = int(input().strip())
if N%2 or (N>=6 and N<=20):
    print("Weird")
else:
    print("Not Weird")
#!/bin/python3
number = int(input())
if ((number%2 != 0) or ((number%2 == 0) and (6 <= number <= 20))):
	print ('Weird')
elif ((number%2 == 0) and ((2 <= number <= 5) or (number > 20))) :
	print ('Not Weird')
#!/bin/python3
import sys
N = int(input().strip())
if N%2==1:
    print("Weird")
elif N%2!=1 and N>=2 and N<=5:
    print ("Not Weird")
elif N%2!=1 and N>=6 and N<=20:
    print ("Weird")
elif N%2!=1 and N>20:
    print ("Not Weird")
#!/bin/python3
import sys
N = int(input().strip())
if N % 2 == 1 or N >= 6 and N <= 20:
    print("Weird")
elif N >= 2 and N <= 5 or N >= 20:
    print("Not Weird")
#!/bin/python3
import sys
N = int(input().strip())
x=N%2
if (x!=0):
    print("Weird")
# elif (x==0):

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
