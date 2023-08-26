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
for i in range(len(s)):
    if s[i] in vowels:
        kevsc += (len(s)-i)
    else:
        stusc += (len(s)-i)

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

kev = 0
stu = 0

for i in range(len(s)):
    if s[i] in vowels:
        kev += (len(s)-i)
    else:
        stu += (len(s)-i)

if kev > stu:
    print("Kevin", kev)
elif kev < stu:
    print("Stuart", stu)
else:
    print("Draw")


def minion_game(string):
    kevinScore, stuartScore = [0, 0]
    for i in range(len(string)):
        if string[i] in "AEIOU":
            kevinScore += len(string)-i
        else:
            stuartScore += len(string)-i
    if stuartScore == kevinScore:
        print("Draw")
    elif stuartScore > kevinScore:
        print("Stuart {}".format(stuartScore))
    else:
        print("Kevin {}".format(kevinScore))

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
    print("Kevin", kevsc)
elif kevsc < stusc:
    print("Stuart", stusc)
else:
    print("Draw")

S = list(input())
#S = "BFEREZKMEYKTNZZTCVZRWZSIIRLEUWGXROAHKCRZNZKUUFWEDJVPMGNGDVHNIGUNKDAUFOIYXVMVBNBMLDQAYJSXNJFVZCERKWJXYUHHLYEBBVRQTXJMGVNFKYHHPZGZOLIBDNTHTZPDJNASKAQPCTXETRZBGIPYHZHOUJPBPRCEKTOWENMEHJVEPPKQISJLTWQOLATVIFOBEXUJPMKXGUDFHBEGMFCCUXBJMXFOKRCICSPQQFFJZTIHMLURFCCVZYIPYGDTJXGXSUAHOKLVYFMSHOSMNNIIRAUPFAAOQHLQCTUGCMCQMOQUXMYBQXJVYRIIQENPTMBYVOVPFYDOJKVUWKDHDWYNVDAMUBBPNTEZZSDADELGNILAZTTMUMWGKXPSQDYVTGXWGDLAZQIJADPTFIJSLIDTLEJFJGWMOCPYLAFMVHQHRLGSIQJXQQKJAVBMFKEENTJZWBDTDVUBZHVTDFCLLETZJRMYMIQYVWWUOIVPGTNZFNTDKBVZKKFDTSQTVSRAADPWIMXEEJHBFRDDDXMOYEHCUHSBWZLHVCKZKUTVWGNTEPYPNGCDMFNKWGARVDMLZJDPIKLWYULIMBOHVOSWZICGZGBKBODQCVIAVTDZQFYLCRWIQBBGMGGERSLPGYASHNYRVVWAVJYASVATKHQNJNYFCUDXKRDNBWHLRIOFVHVFOJQGGAMKNOVDVKJVBRNAIUBZQEBPWKXZUCIRQDRTRGWKTYIJZNBRGQYKOAQCPCRKKXPAAHWLKSJUJZOOIQCSBPDCWHANQPWSIYDBZFCIEWZKYOMMHCHONSOGVMEGGOUKXLGFVOUSIYFFLZAPTLJYWIQVXZZPYVTAOQFQURGULWGFKBYIKJOCSITSBFRIJINCOBHGZRSFYTXFQRFYCIDLXFCASUQAYTHGNBPFTXLUZIXHNXFJIJQABSGNQDOAWXIDSSMLPHHQXYJGVXEJVDVJNCLLBDAYUQFDRGFAAWMAWZZVDAPLHYDU" #406312
consonants = "bcdfghjklmnpqrstvwxyz".upper()
vowels = "aeiou".upper()
scoreK,scoreS = 0,0
lenS = len(S)
