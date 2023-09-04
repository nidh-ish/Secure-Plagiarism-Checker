#!/usr/bin/env python3

S = input()
length = len(S)
scores = {'Stuart': 0, 'Kevin': 0}
for index, letter in enumerate(S):
  if letter in ['A', 'E', 'I', 'O', 'U']:
    scores['Kevin'] += length - index
  else:
    scores['Stuart'] += length - index
if scores['Kevin'] == scores['Stuart']:
  print('Draw')
else:
  print(max(scores, key=scores.get), max(scores.values()))

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
            
class Person(object):
    def __init__(self,name,parent,children):
  
        self.name=name
        self.parent=parent
        self.children=children