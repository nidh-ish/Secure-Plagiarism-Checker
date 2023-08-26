N = int(input().strip())

if N%2 != 0:
    print('Weird')
elif ( N >=2 and N<=5 ) or (N > 20):
    print('Not Weird')
else:
    print('Weird')


#!/bin/python3

import sys


N = int(input().strip())
if (N%2!=0):
    print("Weird")
    
else:
    if (N>=2 and N<=5):
        print("Not Weird")
    if (N>=6 and N<=20):
        print("Weird")
    if (N>20):
        print("Not Weird")


#!/bin/python3

import sys


N = int(input().strip())

if not N % 2 and (N < 6 or N > 20):
    print('Not Weird')
else:
    print('Weird')

#!/bin/python3a
a= int(input())

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

# if N % 2 != 0:
