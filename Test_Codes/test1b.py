import math

input_1 =  input()
input_2 =  input()
input_1 = int(input_1)
input_2 = int(input_2)
res = math.sqrt((input_1*input_1)+(input_2*input_2))

print (res)

def tsum(limit):
    tsum , k = 0 , 1
    while(k <= limit):
        tsum+=k
        k+=1
    return tsum

def func(n):
    s , i = 0 , 1
    while (i<=n):
        s+=i

a = input()
a = int(a)


if(5 <= a < 18):
 print("child")
elif(a >= 18):
 print("adult")
elif(a < 5):
 print("infant")
