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
    elif Kevin < Stuart:
        print('Stuart',Stuart)
    else:
        print('Draw')


import sys
s = sys.stdin.readline()

vowel = "AEIOU"
sc = 0
kc = 0
for i in range(len(s)):
    if s[i] in vowel:
        kc += (len(s) - i)
    else:
        sc += (len(s) - i)

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
