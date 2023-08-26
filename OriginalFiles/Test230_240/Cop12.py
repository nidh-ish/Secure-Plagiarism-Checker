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
else:
    print('Stuart',stuart_point)

S = input()
score_S = 0
score_K = 0
for i in range(len(S)):
        if S[i] in "AEIOU":
            score_K += (len(S)-i) 
        else :
            score_S += (len(S)-i) 
            
if score_K>score_S:
    print('Kevin',score_K,sep=' ')
    
elif score_S>score_K:
    
    print('Stuart',score_S,sep=' ')
else:
    print('Draw')



S = input()
s=0
k=0
for i in range(len(S)):
    if S[i]=='A' or S[i]=='E' or S[i]=='I' or S[i]=='O' or S[i]=='U':
        k+=len(S)-i
    else:
        s+=len(S)-i
if s==k:
    print("Draw")
elif k>s:
    print("Kevin "+ str(k))
else:
    print("Stuart "+ str(s))


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

# Enter your code here. Read input from STDIN. Print output to STDOUT
N=input()
for i in range(0,N):
    print(i*i)


n = int(input())

for i in range(n):
    print(i**2)


# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(0, n):
    print(i * i)

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

for i in range(n):
    print(i**2)

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())

if N >= 1 & N <= 20:
    i = 0
    while i < N:
        print(i**2)
