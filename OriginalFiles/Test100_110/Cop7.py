# else:
	# print ('Draw')

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
    else:
        print("Draw")

string = input()
Stuart = 0
Kevin = 0
strlen = 1
vowels = ("a","e","i","o","u")
for i in range(len(string)):
    if string[i].lower() in vowels:
        Kevin += (len(string)-i)
