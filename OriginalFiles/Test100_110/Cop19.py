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
