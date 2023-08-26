import sys


N = int(input().strip())
if N % 2 == 0 and (  N in range(2,6) or N >20):
    print('Not Weird')
elif N % 2 == 0 and  N in range(6,20):
    print('Weird')
else:
    print ('Weird')


#!/bin/python3

import sys


n = int(input().strip())
if (n % 2 == 1):
    print ('Weird')
else:
    if (2<= n <= 5):
        print ('Not Weird')
    elif (6<= n <= 20):
        print ('Weird')
    elif (n> 20):
        print ('Not Weird')
        

#!/bin/python3

import sys


N = int(input().strip())
if not(N%2==0): 
    print("Weird")
elif N<5: 
    print("Not Weird")
elif N<21:
    print("Weird")
else: 
    print("Not Weird")


#!/bin/python3

import sys


N = int(input().strip())

if N%2 != 0 :
    print ('Weird')
elif N%2 == 0 and 2<N<5:
    print('Not Weird')
elif N%2 ==0 and 6<N<=20:
    print('Weird')
elif N%2 == 0 and N>20:
    print('Not Weird')

#!/bin/python3

import sys



N = int(input().strip())
if(N%2==0) :
    if (N<5 or N>20):
        print('Not Weird')
    else :
        print ("Weird")
else :
    print ("Weird")

#!/bin/python3

import sys


N = int(input().strip())
if (N%2 == 0):
    if (6<=N<=20):
        print ("Weird")
    else:
        print ("Not Weird")
else:
    print ("Weird")

n=int(input())
if(n%2 == 1):
    print("Weird")
elif(n%2==0 and n>=2 and n<=5):
    print("Not Weird")
elif(n%2==0 and n>=6 and n<=20):
    print("Weird")
elif(n%2==0 and n>20):
    print("Not Weird")
else:
    print("")

#!/bin/python3

import sys


N = int(input().strip())
if N%2!=0:
    print("Weird")
elif 2<=N<=5:
    print("Not Weird")
elif 6<=N<=20:
    print("Weird")
elif N>20:
    print("Not Weird")

#!/bin/python3

import sys


n = int(input().strip())

if n % 2 == 1:
    print('Weird')
    
else:
    if n in range(2,6):
        print('Not Weird')
    
    elif n in range(6,21):
        print('Weird')
     
    else:
        print('Not Weird')

#!/bin/python3

import sys


N = int(input().strip())
if N%2 == 1 or (N>=6 and N <=20):
    print("Weird")
else:
    print("Not Weird")

#!/bin/python3

import sys


N = int(input().strip())
if (N % 2) != 0:
    print("Weird")
if (N % 2 == 0 and N >= 2 and N <= 5):
    print("Not Weird")
if (N % 2 == 0 and N >= 6 and N <= 20):
    print("Weird")
if (N % 2 == 0 and N > 20):
    print("Not Weird")

#!/bin/python3

import sys
n = int(input().strip())

message = "Weird" if n % 2 != 0  else "Not Weird" if 2 <= n <= 5 else "Weird" if 6 <= n <= 20 else "Not Weird"
print(message)

#!/bin/python3

