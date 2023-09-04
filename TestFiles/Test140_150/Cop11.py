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
s = input().strip().upper()
vowels = 'AEIOU'
score = {'Stuart':0, 'Kevin':0}
for x in range(len(s)):
    if s[x] in vowels:
        score['Kevin'] += len(s) - x
    else:
        score['Stuart'] += len(s) - x
print(score, file=stderr)
if score['Kevin'] != score['Stuart']:
    winner = max(score,key=score.get)
    print(winner,score[winner])
else:
    print('Draw')
s = input().strip()
s_length = len(s)
vowel_list = ['A','E','I','O','U']
stuart_point = 0
kevin_point = 0
for i in range(s_length):
    if s[i] in vowel_list:
        kevin_point += s_length - i
    else:
        stuart_point += s_length - i
if stuart_point == kevin_point:
    print('Draw')
elif kevin_point > stuart_point:
    print('Kevin',kevin_point)

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