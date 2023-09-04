
print('Stuart',stuart_point)
S = input()
score_S = 0
score_K = 0
for i in range(len(S)):
        if S[i] in "AEIOU":
            score_K += (len(S)-i) 
        else :
            score_S += (len(S)-i) 
if score_K>score_S:
    print('Kevin',score_K,sep=' ')
elif score_S>score_K:
    print('Stuart',score_S,sep=' ')
else:
    print('Draw')
S = input()
s=0
k=0
for i in range(len(S)):
    if S[i]=='A' or S[i]=='E' or S[i]=='I' or S[i]=='O' or S[i]=='U':
        k+=len(S)-i
    else:
        s+=len(S)-i
if s==k:
    print("Draw")
elif k>s:
    print("Kevin "+ str(k))
else:
    print("Stuart "+ str(s))
    # your code goes here
def minion_game(string):
    vowel =['A','E','I','O','U']
    S=0
    K=0
    for i in range(len(string)):
        if string[i] in vowel:
            K+= len(string)-i
        else:
            S+=len(string)-i
    if S>K:
        print("Stuart"+" "+ "%d" % S)
    elif K>S:
        print("Kevin"+" "+'%d' % K)
    else:
        print("Draw")
N=input()
for i in range(0,N):
    print(i*i)
n = int(input())
for i in range(n):
    print(i**2)
n = int(input())
for i in range(0, n):
    print(i * i)
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