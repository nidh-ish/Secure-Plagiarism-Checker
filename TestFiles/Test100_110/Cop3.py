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
S = "BFEREZKMEYKTNZZTCVZRWZSIIRLEUWGXROAHKCRZNZKUUFWEDJVPMGNGDVHNIGUNKDAUFOIYXVMVBNBMLDQAYJSXNJFVZCERKWJXYUHHLYEBBVRQTXJMGVNFKYHHPZGZOLIBDNTHTZPDJNASKAQPCTXETRZBGIPYHZHOUJPBPRCEKTOWENMEHJVEPPKQISJLTWQOLATVIFOBEXUJPMKXGUDFHBEGMFCCUXBJMXFOKRCICSPQQFFJZTIHMLURFCCVZYIPYGDTJXGXSUAHOKLVYFMSHOSMNNIIRAUPFAAOQHLQCTUGCMCQMOQUXMYBQXJVYRIIQENPTMBYVOVPFYDOJKVUWKDHDWYNVDAMUBBPNTEZZSDADELGNILAZTTMUMWGKXPSQDYVTGXWGDLAZQIJADPTFIJSLIDTLEJFJGWMOCPYLAFMVHQHRLGSIQJXQQKJAVBMFKEENTJZWBDTDVUBZHVTDFCLLETZJRMYMIQYVWWUOIVPGTNZFNTDKBVZKKFDTSQTVSRAADPWIMXEEJHBFRDDDXMOYEHCUHSBWZLHVCKZKUTVWGNTEPYPNGCDMFNKWGARVDMLZJDPIKLWYULIMBOHVOSWZICGZGBKBODQCVIAVTDZQFYLCRWIQBBGMGGERSLPGYASHNYRVVWAVJYASVATKHQNJNYFCUDXKRDNBWHLRIOFVHVFOJQGGAMKNOVDVKJVBRNAIUBZQEBPWKXZUCIRQDRTRGWKTYIJZNBRGQYKOAQCPCRKKXPAAHWLKSJUJZOOIQCSBPDCWHANQPWSIYDBZFCIEWZKYOMMHCHONSOGVMEGGOUKXLGFVOUSIYFFLZAPTLJYWIQVXZZPYVTAOQFQURGULWGFKBYIKJOCSITSBFRIJINCOBHGZRSFYTXFQRFYCIDLXFCASUQAYTHGNBPFTXLUZIXHNXFJIJQABSGNQDOAWXIDSSMLPHHQXYJGVXEJVDVJNCLLBDAYUQFDRGFAAWMAWZZVDAPLHYDU" #406312
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

class RegularPolygon(Shape):
  def __init__(self, n, l, name="Regular Polygon"):
    if(n < 3):
      raise ValueError("Polygons can't have less than 3 sides.")
    Shape.__init__(self, name)
    self.num_of_sides = n
    self.length = l

  def area(self):
    theta = 2 * math.pi / self.num_of_sides
    phi = (self.num_of_sides - 2) * math.pi / (2 * self.num_of_sides)
    b = self.length
    h = (b * math.tan(phi)) / 2
    area_triangle = 0.5 * b * h
    return self.num_of_sides * area_triangle
