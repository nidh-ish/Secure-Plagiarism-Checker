if kevin > stuart:
    print("Kevin", kevin)
elif kevin < stuart:
    print("Stuart", stuart)
else:
    print("Draw")

def Kevin(string):
    if string[0] in ['a','e','i','o','u']:
        return True
    else: return False
    

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
