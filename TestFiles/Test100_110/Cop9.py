if count1>count2:
    print('Kevin'+' '+str(count1))
elif count2>count1:
    print('Stuart'+' '+str(count2))
else:
    print('Draw')
def minion_game(string):    
    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(string)):
        if s[i] in vowels:
            kevsc += (len(string)-i)
        else:
            stusc += (len(string)-i)
    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")
word = input().strip()
vowels = ['A','E','I','O','U']
vCount = 0
cCount = 0
for i in range(len(word)):
    if word[i] in vowels:
        vCount += len(word) - i
    else:
        cCount += len(word) - i
if cCount == vCount:
    print('Draw')
elif cCount > vCount:
    print("Stuart "+str(cCount))  
else:
    print("Kevin "+str(vCount))
def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    lgth = len(string)
    stu = kev = 0
    for num, i in enumerate(string):
        if i in vowels:
            kev += lgth - num
        else:
            stu += lgth - num
    if kev > stu:
        print('Kevin {}'.format(kev))
    elif stu > kev:
        print('Stuart {}'.format(stu))
    else:
        print('Draw')
def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    kevin = 0
    stuart = 0
    n = len(string)
    for i in range(len(string)):
        if string[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i
    if kevin == stuart:
        print('Draw')
    elif kevin > stuart:
        print('Kevin', kevin)
    else:
        print('Stuart', stuart)
def minion_game(s):
    stu=0
    kev=0
    length=len(s)
    for i in range(length):
        if not s[i] in ['A','E','I','O','U']:
            stu+=length-i
        else:
            kev+=length-i
    if(stu>kev):
        print("Stuart", stu)
    elif(kev>stu):
        print("Kevin",kev)
    else:
        print("Draw")
def minion_game(string):
    vowel =['A','E','I','O','U']
    S=0
    K=0
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