if(a%2==1):
       print("Weird")  
elif(a%2==0 and a>=2 and a<=5):
    print("Not Weird")
elif(a%2==0 and a>=6 and a<=20):
    print("Weird")
elif(a%2==0 and a>20):
    print("Not Weird")

#!/bin/python3

import sys


N = int(input().strip())
if N % 2 != 0:
    print ("Weird")
else:
    if N >=2 and N <= 5:
        print ("Not Weird")
    elif N >= 6 and N <= 20:
        print ("Weird")
    else:
        print ("Not Weird")


#!/bin/python3

import sys


N = int(input())
if N%2==1:
    print('Weird')
else:
    if N in range(2,6) or N>20:
        print('Not Weird')
    elif N in range(6,21):
        print('Weird')
        
    

#!/bin/python3

import sys


N = int(input().strip())

if N % 2 == 1:
    print("Weird")

if 2 <= N <= 5 and N % 2 == 0: 
    print("Not Weird")
if N % 2 == 0 and 6 <= N <= 20:
    print("Weird")
if N > 20 and N % 2 == 0:
    print("Not Weird")


#!/bin/python3

import sys


N = int(input().strip())

if N % 2 != 0:
    print('Weird')
else:
    if 2<=N and N<=5:
        print('Not Weird')
    elif 6<=N and N<=20:
        print('Weird')
    elif N > 20:
        print('Not Weird')


#!/bin/python3

import sys


N = int(input().strip())

if N % 2 == 0:
    if N >= 2 and N <= 5:
        print("Not Weird")
    elif N >= 6 and N <= 20:
        print("Weird")
    elif N > 20:
        print("Not Weird")
else:
    print("Weird")

#!/bin/python3

import sys


N = int(input().strip())

if N % 2 == 0:
    if N in range(2,6) or N > 20:
        print('Not Weird')
    else:
        print('Weird')
else:
    print('Weird')    

#!/bin/python3

import sys


N = int(input().strip())

if (N%2 != 0) :
    print("Weird\n")
elif ((N%2 == 0) and (N>=2 and N<=5)) :
    print("Not Weird\n")
elif ((N%2 == 0) and (N>=6 and N<=20)) :
    print("Weird\n")
elif ((N%2 == 0) and (N>20)) :
    print("Not Weird\n")


#!/bin/python3

import sys


N = int(input().strip())
if N%2 != 0:
    print("Weird")
else:
    if N>=2 and N<=5:
        print("Not Weird")
    elif N>=6 and N<=20:
        print("Weird")
    else:
        print("Not Weird")

#!/bin/python

import sys


N = int(input().strip())
if N%2!=0:
    print("Weird")
elif N>=2 and N<=5:
         print("Not Weird")
elif N>=6 and N<=20:
        print("Weird")
else:
    print("Not Weird")

#!/bin/python3

import sys


n = int(input().strip())

if n % 2 == 1:
    print("Weird")
else:
    if n >= 6 and n <= 20:
        print("Weird")
    else:
        print("Not Weird")

#!/bin/python3

