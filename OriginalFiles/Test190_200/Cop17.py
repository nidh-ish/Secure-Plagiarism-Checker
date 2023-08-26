n = int(input())

for i in range(n):
    print(i**2)

# Enter your code here. Read input from STDIN. Print output to STDOUT

N=int(input())
for i in range(0,N):
    print(i**2)

a=input()
for i in range(a):
    print(pow(i,2))
   

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
for i in range(0,a):
    print(i**2)

#!/bin/python3

import sys


n = int(input().strip())
if n % 2 == 0:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")
else:
    print("Weird")

N=int(input().strip())
if((N>=1)and(N<=100)):
    if(N%2==1):
        print("Weird")
    elif(N<=5):
        print("Not Weird")
    elif(N<=20):
        print("Weird")
    else:
        print("Not Weird")


#!/bin/python3

import sys


N = int(input().strip())
if N%2!=0 and N<=100: print('Weird')
if N%2==0 and N>=2 and N<=5 : print ('Not Weird')
if N%2==0 and N>5 and N<=20 : print ('Weird')
if N%2==0 and N>=21 and N<=100: print ('Not Weird')

#!/bin/python3

import sys
N = int(input().strip())
if N%2==1:
    print('Weird')
elif N>20:
    print('Not Weird')
elif N>5:
    print('Weird')
elif N>1:
    print('Not Weird')
    


#!/bin/python3

import sys


N = int(input().strip())
res = "Weird"

if N%2 == 0:
    if N<= 5 or N > 20:
        res = "Not Weird"
        
print(res)
    


#!/bin/python3

import sys


N = int(input().strip())

if(N%2 or 6<=N<=20):
    print("Weird")
else:
    print("Not Weird")

#!/bin/python3

import sys

N = int(input().strip())

if N%2==0:
    if N<6 and N>1:
        print('Not Weird')
    if N>6 and N<21:
        print('Weird')
    if N>20:
        print('Not Weird')
else:
    print('Weird')


#!/bin/python3

import sys

N = int(input().strip())
even = (N % 2 == 0)
if(not even or (N >= 6 and N <= 20)):
    print("Weird")
elif(even and ((N >= 2 and N <= 6) or N > 20)):
    print("Not Weird")
    

#!/bin/python3

import sys


N = int(input().strip())

if (N % 2 == 1):
    print("Weird")
elif (N >1 and N <5): 
    print("Not Weird")
elif (N >5 and N <21): 
    print("Weird")
else:
    print("Not Weird")

#!/bin/python3

import sys


N = int(input().strip())
if N%2!=0:
    print ("Weird")
else:
    if N>=2 and N<=5:
        print ("Not Weird")
    if N>=6 and N<=20:
        print ("Weird")
    if N>20:
        print ("Not Weird")


#!/bin/python3

import sys


N = int(input().strip())

if N % 2:
    print("Weird")
    exit(0)

if N >= 2 and N <= 5:
    print("Not Weird")

if N >= 6 and N <= 20:
    print("Weird")

if N > 20:
    print("Not Weird")


#!/bin/python3

import sys


