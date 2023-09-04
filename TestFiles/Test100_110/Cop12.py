def minion_game(string):
    # your code goes here
       vowels = 'AEIOU'

       kevin, stuart = 0, 0

       for i in range( len(string) ):
              if string[i] in vowels:
                     kevin += len(string) - i
              else:
                     stuart += len(string) - i

       if kevin > stuart:
              print( "Kevin " + str(kevin) )
       elif stuart > kevin:
              print("Stuart " + str(stuart) )
       else:
              print("Draw")        
vowels = set("AEIOU")
str = input()
kevin = 0
stuart = 0
for i in range(len(str)):
    if str[i] in vowels:
        kevin += len(str) - i
    else:
        stuart += len(str) - i
if kevin == stuart:
    print("Draw")
elif kevin > stuart:
    print("Kevin {0}".format(kevin))
else:
    print("Stuart {0}".format(stuart))
def minion_game(s):
    s = s.upper()
    # your code goes here
    r = [0,0]
    for i,c in enumerate(s):
        r[c in 'AEIOU'] += len(s) - i
    if r[0] > r[1]:
        print("Stuart", r[0])
    elif r[1] > r[0]:
        print("Kevin", r[1])
    else:
        print("Draw")
def minion_game(string):
    #print(string)
    n = len(string)
    vow_score = 0
    con_score = 0
    for j in range(n):
        if string[j] in 'AEIOU':
            vow_score += n - j
        else:
            con_score += n - j
    if vow_score > con_score:
        print('Kevin', vow_score)
    elif vow_score < con_score:
        print('Stuart', con_score)
    else:
        print('Draw')
def minion_game(string):
    string = string.upper()
    vowels = ['A', 'E', 'I', 'O', 'U']
    kevin_score, stuart_score = 0, 0
    for i in range(0, len(string)):
        if string[i] in vowels:
            kevin_score = kevin_score + len(string) - i
        else:
            stuart_score = stuart_score + len(string) - i
    if stuart_score > kevin_score:
        print('Stuart {}'.format(stuart_score))
    elif stuart_score < kevin_score:
        print('Kevin {}'.format(kevin_score))
    else:
        print('Draw')
a = input()
stu = 0
kel = 0
n = len(a)
for i in range(n):
    if a[i] in 'AEIOU':
        kel += n-i
    else:
        stu += n-i
if kel > stu:
    print('Kevin '+str(kel))
elif stu >kel:
    print('Stuart '+str(stu))
else:
    print('Draw')
from sys import stderr
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