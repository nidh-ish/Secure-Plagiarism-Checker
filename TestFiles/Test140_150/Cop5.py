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
st=input()
s=k=0
l=len(st)
for i in range(l):
    if st[i] in ('A','E','I','O','U'):
        k+=l-i
    else:
        s+=l-i
if s>k:
    print("Stuart",s)
elif k>s:
    print("Kevin",k)
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
    print("Kevin " + str(kevsc))
elif kevsc < stusc:
    print("Stuart " + str(stusc))
else:
    print("Draw")
S = input()
vowel = const = 0
vowels = ['A', 'E', 'I', 'O', 'U']
for passes, item in enumerate(S):
    if item in vowels:
        vowel += len(S) - passes
    else:
        const += len(S) - passes
if vowel > const:
    print('Kevin {}'.format(vowel))
elif vowel < const:
    print('Stuart {}'.format(const))
else:
    print('Draw')
def minion_game(string):
    scores = {"Stuart": 0, "Kevin": 0}
    for i in range(len(string)):
        score = len(string)-i
        if string[i] in "AEIOU":
            scores["Kevin"] += score
        else:
            scores["Stuart"] += score
    if scores["Kevin"] == scores["Stuart"]:
        print("Draw")
    else:
        print(*max(scores.items(), key=lambda x: x[1]))
def minion_game(string):
    # your code goes here
    kevsc=0
    stusc=0
    vowels = 'AEIOU'
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
    
def minion_game(string):
    lenstr = len(string)
    num1=0
    num2=0
    index = 0
    for a in string:
        if (a.lower()=='a' or a.lower()=='e' or a.lower()=='i' or a.lower()=='o' or a.lower()=='u'):
            num1 += lenstr-index
        else:
            num2 += lenstr-index
        index += 1
    if num1 > num2: 
        print("Kevin",num1)
    elif num1 < num2:
        print("Stuart",num2)
    else:
        print("Draw")
String = input().strip()
VOWELS = "AEIOU"
kevsc = 0
stusc = 0
for i in range(len(String)):
    if String[i] in VOWELS:
        kevsc += (len(String)-i)
    else:
        stusc += (len(String)-i)
if kevsc > stusc:
    print ("Kevin",kevsc)
elif kevsc < stusc:
    print ("Stuart",stusc)
else:
    print ("Draw")
def minion_game(s):
    N = len(s)
    Kevin = sum([i for i in range(1,N+1) if s[-i] in 'AEIOU'])
    Stuart = N*(N+1)//2 - Kevin
    if Kevin > Stuart:
        print('Kevin',Kevin)

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
class RegularPolygon(Shape):
  def __init__(self, n, l, name="Regular Polygon"):
    Shape.__init__(self, name)