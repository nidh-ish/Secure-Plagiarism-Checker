# 238 -> 
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
            # ++score
            score += 1
    return score

def minion_game(string):
    k, n = 0, 0
    l = len(string)
    for i in range(l):
        if string[i] in Con:
            k += l-i
        elif string[i] in Vow:
            n += l-i
    if k > n:
        print('Stuart', k)
    elif k < n:
        print('Kevin', n)
    else:
        print('Draw')
            