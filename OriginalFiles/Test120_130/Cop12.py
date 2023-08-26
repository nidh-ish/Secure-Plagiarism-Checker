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
    
    #remove all duplicates
    while max(listNum) == maxItem:
        listNum.remove(maxItem)
    #print(listNum)
    
#print out new max (2nd max)
print(max(listNum))
    

i = int(input())
lis = list(map(int,input().strip().split()))[:i]
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print(max(lis))

iter= int(input())
lt2=(str(input())).split()
lt=[int(i) for i in lt2]
lt.sort()
lt.reverse()
c=lt.count(lt[0])
for i in range(c):
    lt.remove(lt[0])
print(lt[0])


input()
ls = list(map(int, input().strip().split()))
ls.sort()
mx = max(ls)
print(max([x for x in ls if x != mx ]))

N=int(input())
lis=[]
for x in input().split():
    val=int(x);
