import sys


n = int(input().strip())
if (n>20):
    if(n%2==0):
        print("Not Weird")
    else:
        print("Weird")
        
else:
    if(n%2==0):
        if n in range(2,6):
            print("Not Weird")
        else:
            print("Weird")
    else:
        print("Weird")
            


#!/bin/python3

import sys


N = int(input().strip())

if (N%2 != 0) | ((N>= 6) & (N <= 20)) :
    print( "Weird")
else:
    print( "Not Weird")

#!/bin/python3

import sys


N = int(input().strip())

if (N%2 != 0): print ("Weird")   
else:
    if(N<=5): print("Not Weird")
    elif(N>5 and N<=20): print("Weird")
    else: print("Not Weird")
    


N = int(input())
if (N%2!=0) or (N%2==0 and N>=5 and N<=20):
    print ("Weird")
else:
    print ("Not Weird")

#!/bin/python3

import sys


N = int(input().strip())
weird = 'Weird'
not_weird = 'Not Weird'

if N % 2 != 0:
    print(weird)
elif N >= 2 and N <= 5 and N % 2 == 0:
    print(not_weird)
elif N >= 6 and N <= 20 and N % 2 == 0:
    print(weird)
elif N >= 20 and N % 2 == 0:
    print(not_weird)

#!/bin/python3

import sys


N = int(input().strip())

if N%2 != 0:
    print('Weird')
else:
    if N > 1 and N < 6:
        print('Not Weird')
    elif N > 5 and N < 21:
        print('Weird')
    elif N > 20:
        print('Not Weird')

#!/bin/python3

import sys


N = int(input().strip())

if(N % 2 == 1):{
   print("Weird")
    }
elif(N < 6):
    {
    print("Not Weird")
    }
elif(N< 21):
    {
        print ("Weird")
    }
else: print("Not Weird")

#!/bin/python3

import sys

