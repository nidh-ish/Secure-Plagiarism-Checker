if (N%2)==0 and N>=6 and N<=20:
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

if N % 2 != 0 or (N % 2 == 0 and N in range(6, 21)):
    print('Weird')
elif (N % 2 == 0 or N > 20) or (N % 2 == 0 and N in range(2, 6)):
    print('Not Weird')

#!/bin/python3

import sys


N = int(input().strip());
if N%2!=0 :
    print("Weird");
elif (N>=6 and N<=20) :
    print("Weird");
else :
    print("Not Weird");


#!/bin/python3

import sys


N = int(input().strip())

if N % 2 == 1:
    print('Weird')
elif N in range(6, 21):    
    print('Weird')
else:
    print('Not Weird')


#!/bin/python3

import sys


N = int(input().strip())
if(N%2 == 0):
    if(N>=2 and N<=5):
        print("Not Weird")
    elif(N>=6 and N<=20):
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")
        



from itertools import groupby

s = input()

print(*[(len(list(g)), int(k)) for k,g in groupby(s)])

from itertools import groupby
s = input().strip()
res = [(len(list(g)),int(k)) for k,g in groupby(s)]
print(" ".join(map(str, res)))

from itertools import groupby

chars=input()
##chars=sorted(input())

for key,group in groupby(chars):
    print(tuple((len(list(group)),int(key))), end=' ')

   
from itertools import groupby

S = input()
# for c, X in groupby(S):
