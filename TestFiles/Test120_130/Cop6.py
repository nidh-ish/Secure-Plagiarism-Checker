from itertools import groupby
line = input()
for i, j in groupby(line):
    result = (len(list(j)), int(i))
    print(result, end=' ')
from itertools import groupby
S = input()
print(*[(len(list(g)), int(k)) for k, g in groupby(S)], sep=" ")
n = int(input())
line = input().split(' ')
lis = []
for i in line:
    lis.append(int(i))
# lis = [5, 7, 1, 3, 9, 6]
lis.sort()
largest = lis.pop()
while(True):
    try:
        lis.remove(largest)
    except:
        print(lis.pop())
        break

from itertools import groupby
print(*[(len(list(c)), int(k)) for k, c in groupby(input())])
arr = list(input())
result_arr = list()
while arr:
    count = 1
    for j in range(len(arr)-1):
        if len(arr) != 1:
            if arr[j] == arr[j+1]:
                count+=1
                if j == len(arr)-2:
                    result_arr.append((count, int(arr[j]))) 
            else:
                result_arr.append((count, int(arr[j])))
                break
    if len(arr) == 1:
        result_arr.append((count, int(arr[0]))) 
    arr = arr[count:]
            
for item in result_arr:
    print(item, end=" ")
            
import itertools
s = list(input())
res = [(sum(1 for i in g), int(k)) for k, g in itertools.groupby(s)]
print(*res)
from itertools import groupby
sample = input()
for key, group in groupby(sample):
    print ((len(list(group)), int(key)), end=' ')

from itertools import groupby
data=input()
for k, g in groupby(data):
    print(tuple((len(list(g)),int(k))),end=' ')
s=input().strip()
from itertools import groupby
res =[]
for k, g in groupby(s):
    res.append('({}, {})'.format(len(list(g)), k))
print(' '.join(res))
    
import itertools
string = list(input())
lists = []
for key, group in itertools.groupby(string):
    lists.append((len(list(group)), int(key)))
for i in lists:
    print(i, end=" ")
from itertools import groupby
ls = input()
for k, g in groupby(ls, lambda x: x):
    print('({0}, {1})'.format(len([a for a in g]), k), end =' ')

from itertools import groupby
s = input()
S = groupby(s)
print(*[(len(list(y)), (int(x))) for x, y in S])
S = input()
count = 1
last = "a"
for i in S:
    if int(i) == last:
        count += 1
    else:
        if last == 'a':
            last = int(i)
            count = 1
            
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
