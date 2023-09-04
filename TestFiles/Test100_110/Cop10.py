def minion_game(string):
    vowels = 0
    cons = 0
    for i in range(len(string)):
        if string[i] in 'AEIOU':
            vowels += len(string)-i
        else:
            cons += len(string)-i
    if(vowels>cons):
        print("Kevin " + str(vowels))
    elif(vowels == cons):
        print("Draw")
    else:
        print("Stuart " + str(cons))
def minion_game(string):
    vowels = 'AEIOU'
    kevsc = 0
    stusc = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevsc += (len(string)-i)
        else:
            stusc += (len(string)-i)

    if kevsc > stusc:
        print("Kevin {}".format(kevsc))
    elif kevsc < stusc:
        print("Stuart {}".format(stusc))
    else:
        print("Draw")
d=input()
v=['A','E','I','O','U']
d=list(d)
sf=0
ki=0
kf=t1=t2=0
for i in range(0,len(d)):
    s=k=0
    if d[i] in v:
        k+=1
        t1=len(d)-(i+1)
        ki=t1+k
        kf+=ki
    else:
        s+=1
        t2=len(d)-(i+1)
        si=t2+s
        sf+=si
if sf>kf:
    print('Stuart',sf)
elif kf>sf:
    print('Kevin',kf)
else:
    print('Draw')
def minion_game(string):
    c1=0
    c2=0
    for i in range(len(string)):
        if string[i:i+1] in 'aeiouAEIOU':
            c1=c1+len(string)-i
        else:
            c2=c2+len(string)-i
    if c1>c2:
        print('Kevin',c1)
    if c2>c1:
        print('Stuart',c2)
    if c1==c2:
        print('Draw')
string = input().strip()
stuart_points = 0
kevin_points = 0
str_length = len(string)
for i in range(str_length):
    ch = string[i]
    if ch in ['A', 'E', 'I', 'O', 'U']:
        kevin_points += (str_length - i)
    else:
        stuart_points += (str_length - i)
if stuart_points > kevin_points:
    print('{0} {1}'.format('Stuart', stuart_points))
elif kevin_points > stuart_points:
    print('{0} {1}'.format('Kevin', kevin_points))
else:
    print('Draw')
string = input()
stuart = 0
kevin = 0
for i in range(len(string)):
    if string[i] in ["A", "E", "I", "O", "U"]:
        kevin += len(string) - i
import math
class Shape:
	def __init__(self,name="Shape"):
		return self.name 
class Triangle(Shape):
	def __init__(self,base,height):
		Shape.__init__(self,name)
		self.height=height
		self.base=base
	def area(self):
		return 1/2.0*self.base*self.height
# code for RegularPolygon is provided below for your use.
class RegularPolygon(Shape):
  def __init__(self, n, l, name="Regular Polygon"):
    if(n < 3):
      raise ValueError("Polygons can't have less than 3 sides.")
    Shape.__init__(self, name)
    self.num_of_sides = n
    self.length = l