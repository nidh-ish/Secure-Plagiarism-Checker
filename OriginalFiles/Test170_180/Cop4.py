if kc > sc:
    print("Kevin", kc)
elif sc > kc:
    print("Stuart", sc)
else:
    print("Draw")


from itertools import combinations as c
s=input()
l=len(s)
a=['A','E','I','O','U']
c,v=0,0
for i in range(l):
    if s[i] in a:
        v+=(l-i)
    else:
        c+=(l-i)
if v>c:
    print("Kevin "+str(v))
elif c>v:
    print("Stuart "+str(c))
else:
    print("Draw")
    

def minion_game(string):
    l = len(string)
    k = 0
    s = 0
    for i, c in enumerate(string):
        if c in 'AEIOU':
            k += l - i
        else:
            s += l - i
    
    if s == k:
        print("Draw")
    elif s > k:
        print("Stuart {}".format(s))
    else:
        print("Kevin {}".format(k))


def minion_game(string):
    v = 'AEIOU'
    s,k = 0,0
    for i in range(len(string)):
        if string[i] in v:
            k += len(string)-i
        else:
            s += len(string)-i
    if s > k:
        print('Stuart ' + str(s))
    elif k > s:
        print('Kevin ' + str(k))
    else:
        print( 'Draw')
    
    

from collections import defaultdict
s = input()
sdict = defaultdict(int)
scoreC = 0
scoreV = 0
for i in range(0,len(s)):
    word = s[i]
    if s[i] in "AEIOU":
        scoreV += len(s) - i
    else:
        scoreC += len(s) - i

if scoreC == scoreV:        
    print("Draw")
elif scoreC > scoreV:
    print("Stuart %d" %scoreC)
else:
    print("Kevin %d" %scoreV)

vowels = set('AEIOU')
stuart = kevin = 0
word = input()
for i, c in enumerate(word):
    if c in vowels:
        kevin += len(word) - i
    else:
        stuart += len(word) - i
if stuart > kevin:
    print('Stuart', stuart)
elif kevin > stuart:
    print('Kevin', kevin)
else:
    print('Draw')

def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    n = len(string)
    Kevin = 0
    for i in range(n):
        if string[i] in vowels:
            Kevin += n - i
    n *= n + 1
    n /= 2
    n = int(n)
    Stuart = n - Kevin
    if Stuart == Kevin:
        print("Draw")
    elif Stuart > Kevin:
        print("Stuart {0}".format(Stuart))
    else:
        print("Kevin {0}".format(Kevin))
        

def minion_game(string):
    vowel='AEIOU'
    S=K=0
    n=len(string)
    for i, v in enumerate(string):
        if v in vowel:
            K+=n-i
        else:
            S+=n-i
    if K>S:
        print('Kevin %d' %K)
    elif K<S:
        print('Stuart %d' %S)
    else:
        print('Draw')
    # your code goes here

s = input()
kev = 0
stu = 0
for i in range(len(s)):
    j = str.find("AEIOU",s[i])
    if j >= 0:
        kev += len(s) - i
    else:
        stu += len(s) - i

if kev > stu:
    print("Kevin {0}".format(kev))
elif stu > kev:
    print("Stuart {0}".format(stu))
else:
    print("Draw")


def minion_game(string):
    # your code goes here
    l = len(string)
    vowels = ['A', 'E', 'I', 'O', 'U']
    stuart, kevin = [0, 0]
    for i in range(l):
        if string[i] in vowels:
            kevin += (l - i)
        else:
            stuart += (l - i)
    if stuart > kevin:
        print('Stuart ' + str(stuart))
    elif stuart == kevin:
        print('Draw')
    else:
        print('Kevin ' + str(kevin))

n = input()
l = len(n)
v,c = 0,0
# for i in range(0,len(n)):
# 	if n[i] in ['A','E','I','O','U']:
