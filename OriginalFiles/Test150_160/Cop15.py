s=list(set([int(i) for i in input().split(' ')]))
s.sort()
print(s[-2])

input()
print(sorted(set([int(x) for x in input().split()]))[-2])


n = int(input())
arr = sorted(list(map(int, input().split(' '))), reverse=True)

p = arr[0]
for x in arr:
    if x != p:
        print(x)
        break
    p = x
    
    

n=int(input())
y=input()
lis=[]
lis=list(map(int,y.split()))
large=lis[0]
large2=-100000
for i in range(1,n):
    if(lis[i]>large):
        large2=large
        large=lis[i]
    elif(large>lis[i]>large2):
        large2=lis[i]
print(large2)

int(input())
a =list(map(int,input().split()))
m = max(a)
while max(a)==m:
    a.remove(max(a))
print(max(a))

 




N=int(input())
a=sorted(list(set(int(x) for x in input().strip().split())), key=int)
print(a[len(a)-2])

num = int(input())
str = input()
numli = []
numli = str.split(' ')
numlist = []
for x in numli:
    numlist.append(int(x))
numlist.sort()
while(numlist[num-1]== numlist[num-2]):
    num = num-1
print(numlist[num-2])

n = input()
a = input().split(' ')
a = [int(i) for i in a]
a = set(a)
a = list(a)
a.sort()
print(a[len(a)-2])


#get input lenght
N = int(input().strip())

#get input
a = [int(x) for x in input().strip().split(' ')]

#get max
maxVal = max(a)

#get second max
secondMaxVal = max([x for x in a if(x < maxVal)])

#print
print(secondMaxVal)

def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]

n = int(input())
question_list = input().split()
question_list = list(map(int, question_list))
question_list.sort()
largest_num = question_list[n-1]
#print(largest_num)
result_list = remove_values_from_list(question_list, largest_num)
print(result_list[-1])

n=int(input())

ls=input().split(' ')
ls=[int(ls[i]) for i in range(0,n)]

print(sorted(list(set(ls)),reverse=True)[1])

input()
_list = [int(x) for x in input().split()]

first_max = None
second_max = None
for i in _list:
    if first_max is None:
        first_max = i
        continue

    if i > first_max:
        second_max = first_max
        first_max = i
        continue

    if i == first_max:
        continue

    if second_max is None:
        second_max = i
        continue

    if i > second_max:
        second_max = i

print(second_max)

N = int(input())
a = input().split(' ')
a = list(map(int,a))
print(max(list(set(a).difference({max(a)}))))

n = int(input())
x = input().split()
y = list(set(x))
y.sort(key=int)
print(y[len(y)-2])


N = int(input())
nums = list(map(int, input().split()))
maxNum = max(nums)
secMax = max([x for x in nums if x != maxNum])
print(secMax)

numOfItems = input()
listNum = list(map(int,input().split()))
#print(listNum)
for i in range(1):
    #find the max item
    maxItem = max(listNum)
    #print(maxItem)
    
