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

