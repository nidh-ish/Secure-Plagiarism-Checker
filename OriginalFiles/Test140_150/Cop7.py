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
for i in range(0,len(n)):
	if n[i] in ['A','E','I','O','U']:
		t = l-i
		v += t
	else:
		t = l-i
		c += t
if c>v:
	print ('Stuart',c)
elif v>c:
	print ('Kevin',v)
else:
	print ('Draw')

def minion_game(string):
    vowels = ["A","E","I","O","U"]
    Stuart, Kevin = 0,0
    size = len(string)
    for n,i in enumerate(string):
        score = size - n
        if i in vowels:
            Kevin = Kevin + score
        else:
            Stuart = Stuart + score
   
    if (Kevin > Stuart):
        print("Kevin", Kevin)
    elif (Kevin < Stuart):
        print("Stuart", Stuart)
    else:
        print("Draw")
             

def minion_game(string):
    vowels =['A', 'E', 'I', 'O', 'U']
    length = len(string)
    stuart = 0
    kevin = 0
    for i in range(len(string)):
        diff = length - i
        if string[i] in vowels:
            kevin += diff
        else:
            stuart += diff
    if stuart > kevin:
        result = 'Stuart {}'.format(stuart)
    elif kevin > stuart:
        result = 'Kevin {}'.format(kevin)
    else:
        result = 'Draw'
    print(result)

s = input()
leng = len(s)
st = 0
kv = 0
for i in range(leng):
    if s[i] in ['A', 'E', 'I', 'O', 'U']:
        kv = kv + leng-i
    else:
        st = st + leng-i
        
if st > kv:
    print("Stuart %d"%st)
elif kv > st:
    print("Kevin %d"%kv)
else:
    print("Draw")
            
            

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
