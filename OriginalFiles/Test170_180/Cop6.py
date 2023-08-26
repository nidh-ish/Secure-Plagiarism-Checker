Ksc, Ssc = 0, 0
for i,c in enumerate(S):
    if c in 'AEIOU':
        Ksc += len(S) - i
    else:
        Ssc += len(S) - i
if Ksc > Ssc:
    print("Kevin", Ksc)
elif Ksc < Ssc:
    print("Stuart", Ssc)
else:
    print("Draw")

def minion_game(string):
    stu = 0;
    kev = 0;
    lst = list(string)
    sz = len(string)
    for i in range(sz):
        if lst[i] in "AEIOU":
            kev = kev + sz - i 
        else:
            stu = stu + sz - i
    
    if kev == stu:
        print("Draw")
    elif kev > stu:
        print("Kevin", kev)
    else:
        print("Stuart", stu)
    # your code goes here

string=input()
count1=0
count2=0
for i in range(0,len(string)):
    if string[i] in('aeiouAEIOU'):
        count1+=len(string)-i
    else:
        count2+=len(string)-i
if count1>count2:
    print('Kevin'+' '+str(count1))
elif count2>count1:
    print('Stuart'+' '+str(count2))
else:
    print('Draw')


def minion_game(string):    
    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(string)):
        if s[i] in vowels:
            kevsc += (len(string)-i)
        else:
            stusc += (len(string)-i)

    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")

word = input().strip()
vowels = ['A','E','I','O','U']

vCount = 0
cCount = 0
for i in range(len(word)):
    if word[i] in vowels:
        vCount += len(word) - i
    else:
        cCount += len(word) - i
  
if cCount == vCount:
    print('Draw')
elif cCount > vCount:
    print("Stuart "+str(cCount))  
else:
    print("Kevin "+str(vCount))

def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    lgth = len(string)
    stu = kev = 0
    for num, i in enumerate(string):
        if i in vowels:
            kev += lgth - num
        else:
            stu += lgth - num
    if kev > stu:
        print('Kevin {}'.format(kev))
    elif stu > kev:
        print('Stuart {}'.format(stu))
    else:
        print('Draw')
    

def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    kevin = 0
    stuart = 0
    n = len(string)

    for i in range(len(string)):
        if string[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i
    
    if kevin == stuart:
        print('Draw')
    elif kevin > stuart:
        print('Kevin', kevin)
    else:
        print('Stuart', stuart)
        

def minion_game(s):
    stu=0
    kev=0
    length=len(s)
    for i in range(length):
        if not s[i] in ['A','E','I','O','U']:
            stu+=length-i
        else:
            kev+=length-i
    if(stu>kev):
        print("Stuart", stu)
    elif(kev>stu):
        print("Kevin",kev)
    else:
        print("Draw")
                   
   
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

def minion_game(string):
    vowels = 0
    cons = 0
    for i in range(len(string)):
        if string[i] in 'AEIOU':
            vowels += len(string)-i
        else:
            cons += len(string)-i

    #print("Vovels: " + str(vowels))
    #print("Cons: " + str(cons))

    if(vowels>cons):
        print("Kevin " + str(vowels))
    elif(vowels == cons):
        print("Draw")
    else:
        print("Stuart " + str(cons))

# def minion_game(string):
