class Person:
 def __init__(self,n,p,c):
  self.name=n
  self.parent=p
  self.children=c

class Family:
 def __init__(self,hf):
  self.headOffamily=hf
 def headOfFamily(self):
  return self.headOffamily
 def allnodes():
  pass
 
player2score = 0
for i in range(0,len(word)):
	if word[i] in vowels:
		player2score += len(word) - i

def check_duplicates(A, p):
    if p >= len(A):
        return A[p]
    elif A[p+1] == A[p]:
        i = p-1
        while i >= 0 and A[i] == A[p]:
            i = i - 1
        return A[i]
    else:
        return A[p]

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1