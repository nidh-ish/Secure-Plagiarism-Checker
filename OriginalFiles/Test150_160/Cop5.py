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

import sys


n = int(input().strip())


if n%2 != 0:
    print ("Weird")
elif n >= 6 and n<=20:
    print ("Weird")
else:
    print ("Not Weird")


#!/bin/python3

import sys


N = int(input().strip())
if N%2==1:
    print("Weird")
else:
    if N>=2 and N<=5:
        print("Not Weird")
    elif N>=6 and N<=20:
        print("Weird")
    elif N>=20:
        print("Not Weird")

#!/bin/python3

import sys


N = int(input().strip())
if N%2 == 1: print ("Weird") 
else: 
    if N <= 5: print ("Not Weird")
    elif N <= 20: print ("Weird")
    else: print ("Not Weird")

#!/bin/python3

import sys


N = int(input().strip())
if N%2==1: print("Weird")
elif N >= 2 and N <= 5: print("Not Weird")
elif N >= 6 and N <= 20: print("Weird")
elif N > 20: print("Not Weird")


#!/bin/python3

import sys
N = int(input().strip())
if N % 2 != 0:
    print("Weird")
else:
    if N > 1 and N < 6:
        print("Not Weird")
    elif N > 6 and N < 21:
        print("Weird")
    elif N > 20:
        print("Not Weird")
    

#!/bin/python3

import sys


N = int(input())

if (N%2) != 0:
    print("Weird")
elif (N%2)==0 and N>=2 and N<=5:
    print("Not Weird")
elif (N%2)==0 and N>=6 and N<=20:
    print("Weird")
elif (N%2)==0 and N>20:
    print("Not Weird")


#!/bin/python3

import sys

N = int(input().strip())

if N % 2 == 0:
    if N >= 2 and N <= 5 or N > 20:
        print('Not Weird')
    else:
        print('Weird')
else:
    print('Weird')

N = int(input().strip())
if( N % 2 != 0):
    print("Weird")
else:
    if(N > 20 or N in range(2, 6)):
        print("Not Weird")
    else:
        print("Weird")

#!/bin/python3

import sys


n = int(input().strip())


if n == 0 or n<0 or n%2 != 0:
    print("Weird")
elif n in range(2,6):
    print("Not Weird")
elif n in range(6,21):
    print("Weird")
elif n>20:
    print("Not Weird")


N = int(input().strip())

# if N % 2 != 0 or (N % 2 == 0 and N in range(6, 21)):
