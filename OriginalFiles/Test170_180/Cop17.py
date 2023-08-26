

#!/bin/python3

import sys

N = int(input().strip())

if N % 2 != 0 :
    print ("Weird")
else :
    if N >= 2 and N <= 5:
        print ("Not Weird")
    else :
        if N >= 6 and N <=20:
            print ("Weird")
        else:
            print ("Not Weird")
    

#!/bin/python3

import sys


N = int(input().strip())
if N%2 == 1:
    print('Weird')
elif N > 1 and N < 6:
    print ('Not Weird')
elif N > 5 and N < 21:
    print ('Weird')
elif N > 20:
    print('Not Weird')

#!/bin/python3

import sys


N = int(input().strip())
if N%2==1:
    print ("Weird");
elif N>=6 and N<=20:
    print ("Weird");
else :
    print ("Not Weird");


#!/bin/python3

import sys


N = int(input().strip())

if (N) % 2 != 0: 
    print("Weird")
elif ((N) % 2 == 0 and N >=2 and N<=5):
    print("Not Weird")
elif ((N) % 2 == 0 and N >=6 and N <=20):
    print ("Weird")
elif ((N) % 2 == 0 and N >= 20):
    print ("Not Weird")

#!/bin/python3

import sys

N = int(input().strip())

if N % 2 == 0:
    if 2<= N <= 5:
        print("Not Weird")
    elif 6 <= N <= 20:
        print("Weird")
    elif N > 20:
        print("Not Weird")
else:
    print("Weird")
            

N = int(input())
if (N%2 != 0) or (N%2==0 and 6<=N<=20):
    print("Weird")

else:
    print("Not Weird")

#!/bin/python3

import sys


n = int(input().strip())

if n % 2 != 0:
    print ( 'Weird' )
elif n >= 6 and n <= 20:
    print ( 'Weird' )
else: 
    print( 'Not Weird')

#!/bin/python3

import sys


N = int(input().strip())

if((N >= 2 and N<=5) and ((N%2) == 0)):
    print("Not Weird")
elif(N >= 21 and ((N%2) == 0)):
    print("Not Weird")    
else:
    print("Weird")


#!/bin/python3

import sys


N = int(input().strip())
if N%2 != 0:
    print("Weird")
else:
    if 2<=N<=5:
        print("Not Weird")
    elif 6<=N<=20:
        print("Weird")
    elif N>20:
        print("Not Weird")
        
        

#!/bin/python3

import sys


N = int(input().strip())

if N%2 != 0:
    print("Weird");
elif N<=5:
    print("Not Weird");
elif N<=20:
    print("Weird");
else:
    print("Not Weird");
    


#!/bin/python3

import sys


N = int(input().strip())

if N % 2 == 1:
    print("Weird")
elif N % 2 == 0 and (N >= 2 and N <= 5):
    print("Not Weird")
elif N % 2 == 0 and (N >= 6 and N <= 20):
    print("Weird")
# else:
