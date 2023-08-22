# import sys
# sys.path.insert(0, 'Output')
# from Outputs import testoutput
from main import *

# listoffiles = ['test1x.py', 'test2y.py', 'nested_for.py', 'test1a.py', 'test1b.py', 
#                'test2a.py', 'test2b.py', 'test3a.py', 'test3b.py', 'test4a.py', 
#                'test4b.py', 'test5a.py', 'test5b.py', 'test6a.py', 'test6b.py', 
#                'test7a.py', 'test7b.py', 'test8a.py', 'test8b.py', 'test9a.py', 
#                'test9b.py', 'test1c.py', 'test5c.py', 'test9c.py']

listoffiles = ['test1x.py', 'test2y.py', 'nested_for.py', 'test1a.py', 'test1b.py', 
               'test2a.py', 'test2b.py', 'test3a.py', 'test3b.py', 'test4a.py', 
               'test4b.py', 'test5a.py', 'test5b.py', 'test6a.py', 'test6b.py', 
               'test7a.py', 'test7b.py', 'test8a.py', 'test8b.py', 
               'test1c.py', 'test5c.py']


# listoffiles = ['test1x.py', 'test2y.py', 'nested_for.py']

with open("Outputs.py", "w") as f:
    f.write("outputs = {\n")

for i in range(len(listoffiles)):
    for j in range(i):
        # if i == 0 and j == 0:
        #     os.system(f"python main.py 1 Test_Codes/{listoffiles[i]} 2 Test_Codes/{listoffiles[j]} > Outputs.py")
        # else:
        os.system(f"python main.py 1 Test_Codes/{listoffiles[i]} 2 Test_Codes/{listoffiles[j]} >> Outputs.py")


with open("Outputs.py", "a") as f:
    f.write("}")