# else:
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

import sys


N = int(input().strip())

if(N % 2 != 0):
    print("Weird")
elif(N % 2 == 0 and N in range(2,6)):
    print("Not Weird")
