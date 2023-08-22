

listoffiles = ['test1x.py', 'test2y.py', 'nested_for.py', 'test1a.py', 'test1b.py', 
               'test2a.py', 'test2b.py', 'test3a.py', 'test3b.py', 'test4a.py', 
               'test4b.py', 'test5a.py', 'test5b.py', 'test6a.py', 'test6b.py', 
               'test7a.py', 'test7b.py', 'test8a.py', 'test8b.py', 'test9a.py', 
               'test9b.py', 'test1c.py', 'test5c.py', 'test9c.py']

listofpairs = []

for i in range(len(listoffiles)):
    for j in range(i):
        filename1 = listoffiles[i]
        filename2 = listoffiles[j]
        listofpairs.append(f"o{filename1[-5:-3]}{filename2[-5:-3]} ")

for i in range(len(listofpairs)):
    if "9" in listofpairs[i]:
        print(listofpairs[i])