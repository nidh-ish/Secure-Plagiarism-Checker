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