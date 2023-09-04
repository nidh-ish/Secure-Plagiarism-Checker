a = [int(x) for x in input().strip().split(' ')]
secondMaxVal = max([x for x in a if(x < maxVal)])
print(secondMaxVal)
def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]
n = int(input())
question_list = input().split()
question_list = list(map(int, question_list))
question_list.sort()
largest_num = question_list[n-1]
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
for i in range(1):
    maxItem = max(listNum)
    while max(listNum) == maxItem:
        listNum.remove(maxItem)
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
    val=int(x)
    if lis.count(val)==0:
       lis.append(val)
lis.sort()
print(lis[len(lis)-2])
input()
l = [int(n) for n in input().split()]
highest = -101
second_highest = -101
for n in l:
	if n > highest:
		second_highest = highest
		highest = n
	elif n >= second_highest and n != highest:
		second_highest = n
print(second_highest)
import fileinput
lines = fileinput.input()
N = int(lines[0])
A = list(set(map(int, lines[1].split(" "))))
A.sort()
print(A[len(A)-2])
n = int(input())
a = list(map(int,input().strip().split()))
a.sort()
m = max(a)
while max(a) == m:
    a.remove(m)
print(a[len(a)-1])
input()
n = set(map(int, input().split()))
print(sorted(n, reverse=True)[1])
input()
print(sorted(list(set(map(int, input().split(' ')))))[-2])
n = int(input())
numbers_list = set(map(int, input().split(' ')))
numbers_list = list(numbers_list)
numbers_list.sort()
print(numbers_list[-2])
lst = input() == 0 or list(map(int, input().split()))
n = max(lst)
while max(lst) == n:
    lst.remove(n)
print(max(lst))
N = int(input())
A = list(map(int,input().split()))
A.sort()
biggest = A.pop()
i = biggest
while i == biggest:
    i = A.pop()
print(i)
n=int(input())
a=[]
a = [int(x) for x in input().split()]
k=set(a)
d=list(k)
d.sort(reverse=True)
print (d[1])

class Shape:
    def __init__(self,name):
        self.name = name
    def get_details(self):
        return self.name + "(" + str(self.area) + "," + str(self.circumference) + ")"               
# your code for class Triangle -- Q.4(a)
class Triangle(Shape):
    def __init__(self,n, b, h, name="Triangle"):
        Shape.__init__(self, name)
        self.b = b
        self.h = h
        self.n = n
        self.n = 3
    def area(self):
        return (1/2)*self.b*self.h
# code for RegularPolygon is provided below for your use.
class RegularPolygon(Shape):
  def __init__(self, n, l, name="Regular Polygon"):
    if(n < 3):
      raise ValueError("Polygons can't have less than 3 sides.")
    Shape.__init__(self, name)
    self.num_of_sides = n
    self.length = l

  def area(self):
    theta = 2 * math.pi / self.num_of_sides
    phi = (self.num_of_sides - 2) * math.pi / (2 * self.num_of_sides)
    b = self.length
    h = (b * math.tan(phi)) / 2
    area_triangle = 0.5 * b * h
    return self.num_of_sides * area_triangle

  def circumference(self):
    return self.num_of_sides * self.length

  def get_side(self):
    return self.length
# your code for class Square -- Q.4(c)
class Square(RegularPolygon):
    def __init__(self, n,s, name="Square"):
        RegularPolygon.__init__(self,n,s,name)
        self.s = s
        self.n = n
    def area(self):
        return RegularPolygon.area
    def circumference(self):
        return RegularPolygon.circumference
# your code for class EquilateralTriangle -- Q.4(c)
class EquilateralTriangle(RegularPolygon):
    def __init__(self, n,l, name="EquilateralTriangel"):
        RegularPolygon.__init__(self,n,l,name)
        self.l = l
        self.n = n
        self.n = 3
    def area(self):
        return RegularPolygon.area
    def circumference(self):
        return RegularPolygon.circumference
# your code for class Pentagon -- Q.4(d) and Q.4(e)
class Pentagon(Triangle,Square):
    def __init__(self,n,s,name="Pentagon"):
        Square.__init__(self,n,s,name)
        Triangle.__init__(self,n,s,(sqrt(3)/2)*s,name)
        RegularPolygon.__init__(self,n,s,name)
        self.s = s
        self.n = n
    def area(self):
        return Triangle.area + Square.area