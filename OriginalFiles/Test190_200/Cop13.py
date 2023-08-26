def minion_game(string):
    # your code goes here
    stuart=0
    kevin=0
    string=string.lower()
    
    #create all possible substrings
    for i in range(0,len(string)):
        hehe=len(string)-i
        if Kevin(string[i]):
            
            kevin+=hehe
        else:
            stuart+=hehe
            
    #3k=sum(kevin.values())
    if stuart>kevin:
        print('Stuart '+str(stuart))
    elif kevin>stuart:
        print('Kevin '+str(kevin))
    else:
        print('Draw')

S=input()
V=['A','E','I','O','U']
cK,cS=0,0
l=len(S)

for i in range(len(S)):
    if S[i] in V:
#        cK+=len(S[i:])
        cK+=l-i
    else:
#        cS+=len(S[i:])
        cS+=l-i

if cK>cS:print('Kevin',cK)
elif cK<cS:print('Stuart',cS)
else:print('Draw')


def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    Stuart = 0
    Kevin = 0
    L = len(s)
    for idx in range(L):
        n = L - idx
        if s[idx] in vowels:
            Kevin = Kevin + n
        else:
            Stuart = Stuart + n
    print("Stuart", Stuart) if Stuart>Kevin else print("Kevin", Kevin) if Kevin>Stuart else print("Draw")

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
    print ("Kevin " +  str(kevsc))
elif kevsc < stusc:
    print ("Stuart " + str(stusc))
else:
    print ("Draw")

def minion_game(string):
    # your code goes here
    vowels = ["A", "E", "I", "O", "U"]
    vMult, uMult = 0, 0
    vScore, uScore = 0, 0
    for letter in string:
        if letter in vowels:
            vMult += 1
        else:
            uMult += 1
        vScore += vMult
        uScore += uMult
    if vScore > uScore:
        print("Kevin", vScore)
    elif uScore > vScore:
        print("Stuart", uScore)
    else:
        print("Draw")

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
# else:
