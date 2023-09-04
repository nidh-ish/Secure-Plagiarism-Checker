def minion_game(string):
    vowels = "AEIOU"
    stuart_score = 0
    kevin_score = 0
    word_length = len(string)
    for i in range(word_length):
        if string[i] in vowels:
            kevin_score += word_length - i
        else:
            stuart_score += word_length - i
    if kevin_score > stuart_score:
        print("Kevin {}".format(kevin_score))
    elif stuart_score > kevin_score:
        print("Stuart {}".format(stuart_score))
    else:
        print("Draw")
def minion_game(string):
    l = len(string)
    i = 0
    Kev = 0
    Stu = 0
    for s in string:
        if s in 'AEIOU':
            Kev += l - i
        else:
            Stu += l - i
        i += 1
    if Kev > Stu:
        print("Kevin {}".format(Kev))
    elif Stu > Kev:
        print("Stuart {}".format(Stu))
    else:
        print("Draw")
string = input()
Stuart = 0
Kevin = 0
strlen = 1
vowels = ("a","e","i","o","u")
for i in range(len(string)):
    if string[i].lower() in vowels:
        Kevin += (len(string)-i)
    else:
        Stuart += (len(string)-i)
if Stuart > Kevin:
    print ("Stuart "+str(Stuart))
elif Stuart < Kevin:
    print ("Kevin "+str(Kevin))
else: 
    print ("Draw")
msg = input()
vowels = "AEIOU"
kevin = 0
stuart = 0
for i in range(len(msg)):
    if msg[i] in vowels:
        kevin += len(msg) - i
    else:
        stuart += len(msg) - i
if kevin > stuart:
    print("Kevin", kevin)
elif stuart > kevin:
    print("Stuart", stuart)
else:
    print("Draw")
input_string = input().strip()
list1=list(input_string)
string = ""
stuart = 0
kevin = 0
for i in range (0,len(list1)):
    if list1[i] in ['a','e','i','o','u','A','E','I','O','U'] :
        kevin = kevin +  len(list1) - (i+1) + 1
    else : 
        stuart = stuart + len(list1) - (i+1) + 1
if kevin > stuart :
    print ("Kevin", kevin)
elif kevin == stuart :
    print ("Draw")
else :
    print ("Stuart", stuart)
def isVowel(letter):
    return(letter in "AEIOU")
def minion_game(string):
    kevinCount = 0
    stuartCount = 0
    for i in range(0,len(string)):
        if(isVowel(string[i])):
            kevinCount += len(string) - i
        else:
            stuartCount += len(string) - i
    
    if (kevinCount > stuartCount):
        print ("Kevin " + str(kevinCount))
    elif (stuartCount > kevinCount):
        print ("Stuart " + str(stuartCount))
    else:
        print ("Draw")
S = input()
Ksc, Ssc = 0, 0
for i,c in enumerate(S):
    if c in 'AEIOU':
        Ksc += len(S) - i
    else:
        Ssc += len(S) - i
if Ksc > Ssc:
    print("Kevin", Ksc)
elif Ksc < Ssc:
    print("Stuart", Ssc)
else:
    print("Draw")
def minion_game(string):
    stu = 0;
    kev = 0;
    lst = list(string)
    sz = len(string)
    for i in range(sz):
        if lst[i] in "AEIOU":
            kev = kev + sz - i 
        else:
            stu = stu + sz - i
    if kev == stu:
        print("Draw")
    elif kev > stu:
        print("Kevin", kev)
    else:
        print("Stuart", stu)
    # your code goes here
string=input()
count1=0
count2=0
for i in range(0,len(string)):
    if string[i] in('aeiouAEIOU'):
        count1+=len(string)-i
    else:
        count2+=len(string)-i
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