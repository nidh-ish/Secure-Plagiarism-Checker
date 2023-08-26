
import itertools

def minion_game(string):
    l = len(string)
    kevin = 0
    stuart = 0
    for i in range(l):
        if string[i] in 'AEIOU':
            kevin += l - i
        else:
            stuart += l - i
    if (kevin > stuart):
        print('Kevin', kevin)
    elif (kevin < stuart):
        print('Stuart', stuart)
    else:
        print('Draw')
            

def minion_game(string):
    stuart = 0
    kevin = 0
    for index,char in enumerate(string.lower()):
        if char in ['a','e','i','o','u']:
            kevin += len(string) - index
        else:
            stuart += len(string) - index
    if stuart > kevin:
        print('Stuart', stuart)
    elif kevin > stuart:
        print('Kevin', kevin)
    else:
        print('Draw')

def minion_game(string):
    v = "AEIOU"
    stuart, kevin = 0, 0
    ln = len(string)

    for i in range(ln):  
        if string[i] in v:
            kevin += ln - i
        else:
            stuart += ln - i
        
    if stuart > kevin:
        print('Stuart', stuart)
    elif stuart == kevin:
        print('Draw')
    else:
        print('Kevin', kevin)

s = input()
vowels = set('AEIOU')
KevinScore = StuartScore = 0
for i in range(len(s)):
    if s[i] in vowels:
        KevinScore += len(s)-i
    else:
        StuartScore += len(s)-i
if KevinScore == StuartScore:
    print("Draw")
else:
    print('Kevin {}'.format(KevinScore) if KevinScore > StuartScore else 'Stuart {}'.format(StuartScore))

s = input()
#words = {}
stuart_score, kevin_score = 0,0
for i in range(0,len(s)):
    is_vowel = s[i] in "AEIOU"
    #for j in range(0,len(s)-i):
        #word = s[i:len(s)-j]        
    if (is_vowel):
        kevin_score += len(s)-i
    else:
        stuart_score += len(s)-i
if (kevin_score > stuart_score):
    print ("Kevin " + str(kevin_score))
elif (stuart_score > kevin_score):    
    print ("Stuart " + str(stuart_score))
else:
    print("Draw")    
        

s = input()

vowels = 'AEIOU'

kevsc = 0
stusc = 0
# for i in range(len(s)):
#     if s[i] in vowels:
