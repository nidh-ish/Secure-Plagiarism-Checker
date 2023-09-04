def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']
def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']
def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score+=1
    return score
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']
def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']
def score_words(words):
    #print (words)
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score +=1
    return score
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']
def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']
def score_words(words):
    score = 0
    for word in words:
        count = 0
        for letter in word:
            if is_vowel(letter):
                count += 1
        score += 1
        if count%2 == 0:
            score += 1
    return score
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']
def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score
def isVowel(s):
    return s=='A' or s=='I' or s=='U' or s=='E' or s=='O'
def minion_game(s):
    pS = 0
    pK = 0
    for i in range(0, len(s)):
        if(isVowel(s[i])):
            pK = pK + len(s) - i
        else:
            pS = pS + len(s) - i
    if(pS > pK):
        print("Stuart", pS)
    elif(pS < pK):
        print("Kevin", pK)
    else:
        print("Draw")
def minion_game(string):
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
s = input()

class Shape:
    def __init__(self,name):
        self.name = name
    def get_details(self):
        return self.name + "(" + str(self.area) + "," + str(self.circumference) + ")"               
# your code for class Triangle -- Q.4(a)
class Triangle(Shape):
    def __init__(self,n, b, h, name="Triangle"):
        Shape.__init__(self, name)
        self.b = b
        self.h = h
        self.n = n
        self.n = 3
    def area(self):
        return (1/2)*self.b*self.h