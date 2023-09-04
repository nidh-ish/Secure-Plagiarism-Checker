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

    for i, c in enumerate(reversed(s), start=1):
        if c in 'AEIOU':
            kevin += i
        else:
            stuart += i

    if stuart > kevin:
        print('Stuart', stuart)
    elif kevin > stuart:
        print('Kevin', kevin)
    else:
        print('Draw')
s = input()
vowels = 'AEIOU'