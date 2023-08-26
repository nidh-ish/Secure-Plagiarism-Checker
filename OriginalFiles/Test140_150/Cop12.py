
print('Stuart',stuart_point)

S = input()
score_S = 0
score_K = 0
for i in range(len(S)):
        if S[i] in "AEIOU":
            score_K += (len(S)-i) 
        else :
            score_S += (len(S)-i) 
            
if score_K>score_S:
    print('Kevin',score_K,sep=' ')
    
elif score_S>score_K:
    
    print('Stuart',score_S,sep=' ')
else:
    print('Draw')



S = input()
s=0
k=0
for i in range(len(S)):
    if S[i]=='A' or S[i]=='E' or S[i]=='I' or S[i]=='O' or S[i]=='U':
        k+=len(S)-i
    else:
        s+=len(S)-i
if s==k:
    print("Draw")
elif k>s:
    print("Kevin "+ str(k))
else:
    print("Stuart "+ str(s))


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

# Enter your code here. Read input from STDIN. Print output to STDOUT
N=input()
for i in range(0,N):
    print(i*i)


n = int(input())

for i in range(n):
    print(i**2)


# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(0, n):
    print(i * i)

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

for i in range(n):
    print(i**2)

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())

if N >= 1 & N <= 20:
    i = 0
    while i < N:
        print(i**2)
        i += 1

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

for i in range(0,n):
    print(i**2)

x = int(input())

i = 0
while i < x:
    answer = i**2
    print(answer)
    i = i + 1

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())

for i in range(a):
    print(pow(i,2))

n=int(input(""))
for i in range (0,n):
    print(i**2)


x = input()
for i in range(x):
    print(i**2)

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

i = 0
while i < n:
    print(pow(i, 2))
    i = i + 1

# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(0,input()):
    print(i*i)

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
i = 0
while i < n:
    print(i*i)
    i = i+1

for i in range(0, input()):
    print(i ** 2)

# Enter your code here. Read input from STDIN. Print output to STDOUT
x = int(input())
for i in range(0,x):
    print(i**2)

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
