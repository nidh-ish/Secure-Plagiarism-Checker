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
for i in range(lenS):
    if S[i] in consonants:
        scoreS = scoreS + lenS - i
    if S[i] in vowels:
        scoreK = scoreK + lenS - i
if scoreS > scoreK:
    print("Stuart "+str(scoreS))
elif scoreS < scoreK:
    print("Kevin "+str(scoreK))
else:
    print("Draw")

def minion_game(string):
    string.upper()
    vowels = "AEIOU"
    Stu, Kev = 0, 0
    Stu = sum([len(string) - i for i in range(len(string)) if string[i] not in vowels])
    Kev = sum([len(string) - i for i in range(len(string)) if string[i] in vowels])
    if Stu > Kev:
        print("Stuart", Stu)
    elif Stu < Kev:
        print("Kevin", Kev)
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

st=input()
s=k=0
l=len(st)
# for i in range(l):
    # if st[i] in ('A','E','I','O','U'):
