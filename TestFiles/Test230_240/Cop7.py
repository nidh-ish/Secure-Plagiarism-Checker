def isVowel(s):
    return s=='A' or s=='I' or s=='U' or s=='E' or s=='O'
def minion_game(s):
    pS = 0
    pK = 0
    for i in range(0, len(s)):
        if(isVowel(s[i])):
            pK = pK + len(s) - i
        else:
            pS = pS + len(s) - i
    if(pS > pK):
        print("Stuart", pS)
    elif(pS < pK):
        print("Kevin", pK)
    else:
        print("Draw")
def minion_game(string):
    vowels = 'AEIOU'
    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)
    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")
s = input()
vowels = 'AEIOU'
kevsc = 0
stusc = 0
for i in range(len(s)):
    if s[i] in vowels:
        kevsc += (len(s)-i)
    else:
        stusc += (len(s)-i)
if kevsc > stusc:
    print ("Kevin", kevsc)
elif kevsc < stusc:
    print ("Stuart", stusc)
else:
    print ("Draw")
import itertools
def minion_game(string):
    l = len(string)
    kevin = 0
    stuart = 0
    for i in range(l):
        if string[i] in 'AEIOU':
            kevin += l - i
        else:
            stuart += l - i
    if (kevin > stuart):
        print('Kevin', kevin)
    elif (kevin < stuart):
        print('Stuart', stuart)
    else:
        print('Draw')
def minion_game(string):
    stuart = 0
    kevin = 0
    for index,char in enumerate(string.lower()):
        if char in ['a','e','i','o','u']:
            kevin += len(string) - index
        else:
            stuart += len(string) - index
    if stuart > kevin:
        print('Stuart', stuart)
    elif kevin > stuart:
        print('Kevin', kevin)
    else:
        print('Draw')
def minion_game(string):
    v = "AEIOU"
    stuart, kevin = 0, 0
    ln = len(string)
    for i in range(ln):  
        if string[i] in v:
            kevin += ln - i
        else:
            stuart += ln - i
        
    if stuart > kevin:
        print('Stuart', stuart)
    elif stuart == kevin:
        print('Draw')
    else:
        print('Kevin', kevin)
s = input()
vowels = set('AEIOU')
KevinScore = StuartScore = 0
for i in range(len(s)):
    if s[i] in vowels:
        KevinScore += len(s)-i
    else:
        StuartScore += len(s)-i
if KevinScore == StuartScore:
    print("Draw")
else:
    print('Kevin {}'.format(KevinScore) if KevinScore > StuartScore else 'Stuart {}'.format(StuartScore))
s = input()
#words = {}
stuart_score, kevin_score = 0,0
for i in range(0,len(s)):
    is_vowel = s[i] in "AEIOU"
    #for j in range(0,len(s)-i):
        #word = s[i:len(s)-j]        
    if (is_vowel):
        kevin_score += len(s)-i
    else:
        stuart_score += len(s)-i
if (kevin_score > stuart_score):
    print ("Kevin " + str(kevin_score))
elif (stuart_score > kevin_score):    
    print ("Stuart " + str(stuart_score))
else:
    print("Draw")    
s = input()
vowels = 'AEIOU'
kevsc = 0
stusc = 0
for i in range(len(s)):
    if s[i] in vowels:
        kevsc += (len(s)-i)
    else:
        stusc += (len(s)-i)
if kevsc > stusc:
    print ("Kevin", kevsc)
elif kevsc < stusc:
    print ("Stuart", stusc)
else:
    print ("Draw")
word = input()
vowels = ['A', 'E', 'I', 'O', 'U']
cscore = 0
vscore = 0
for i in range(len(word)):
    if word[i] in vowels:
        vscore += (len(word)-i)
    else:
        cscore += (len(word) -i)
if vscore > cscore:
    print("%s %s" % ("Kevin", vscore))
elif vscore < cscore:
    print("%s %s" % ("Stuart", cscore))
else:
    print("Draw")
s=input()
stuart=0
kevin=0
vocali='AEIOU'
for i in range(0,len(s)):
    if s[i] in vocali:
         kevin+=len(s)-i
    else:
        stuart+=len(s)-i
if kevin>stuart:
    print("Kevin",kevin)
elif kevin<stuart:
    print("Stuart",stuart)
else:
    print("Draw")
s, v = input(), 'AEIOU'
stuart, kevin, ln = 0, 0, len(s)
for i in range(ln):  
    if s[i] in v:
        kevin += ln - i
    else:
        stuart += ln - i
if stuart > kevin:
    print('Stuart', stuart)
elif stuart == kevin:
    print('Draw')
else:
    print('Kevin', kevin)
def minion_game(string):
    # your code goes here
    n = len(string)
    vowels = ['A','I','E','O','U']
    Kevin_score = 0
    for i in range(n):
        if string[i] in vowels:
            Kevin_score += n - i
    Stuart_score = n * (n + 1) / 2 - Kevin_score
    if Kevin_score > Stuart_score:
        print ('Kevin', int(Kevin_score), sep = ' ')
    elif Kevin_score < Stuart_score:
        print ('Stuart', int(Stuart_score), sep = ' ')
    else:
        print ('Draw')
def minion_game(s):
    stuart = 0
    kevin = 0

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