# import sys
# sys.path.insert(0, 'Output')
# from Outputs import testoutput
from main import *
import os

# listoffiles = ['test1x.py', 'test2y.py', 'nested_for.py', 'test1a.py', 'test1b.py', 
#                'test2a.py', 'test2b.py', 'test3a.py', 'test3b.py', 'test4a.py', 
#                'test4b.py', 'test5a.py', 'test5b.py', 'test6a.py', 'test6b.py', 
#                'test7a.py', 'test7b.py', 'test8a.py', 'test8b.py', 'test9a.py', 
#                'test9b.py', 'test1c.py', 'test5c.py', 'test9c.py']

# listoffiles = ['test1x.py', 'test2y.py', 'nested_for.py', 'test1a.py', 'test1b.py', 
#                'test2a.py', 'test2b.py', 'test3a.py', 'test3b.py', 'test4a.py', 
#                'test4b.py', 'test5a.py', 'test5b.py', 'test6a.py', 'test6b.py', 
#                'test7a.py', 'test7b.py', 'test8a.py', 'test8b.py', 
#                'test1c.py', 'test5c.py']

lengths = {(100 ,110)}

# for i in range(0, 250, 10):
#     x = i, i+10
#     lengths[x] = []

# listoffiles = {30: ['test1a.py', 'test1b.py', 'nested_for.py'], 20: ['test1x.py', 'test2y.py', 'test6a.py']}
listofoutputs = []

# finit = open(os.path.join("Run", "__init__.py"), "w")
for x in lengths:
    i = x[0]
    with open(os.path.join("Run", f"Outputs{i}.py"), "w") as f:
        f.write(f"outputs{i} = {{\n")
    
    # files = listoffiles[i]
    files = [os.path.join(f"OriginalFiles", f"Test{x[0]}_{x[1]}", f) for f in os.listdir(os.path.join("OriginalFiles", f"Test{x[0]}_{x[1]}")) if os.path.isfile(os.path.join("OriginalFiles", f"Test{x[0]}_{x[1]}", f))]

    for m in range(len(files)):
        for j in range(m):
            os.system(f"python main.py 1 {files[m]} 2 {files[j]} >> " + os.path.join("Run", f"Outputs{i}.py"))
            # os.system(f"python winnowing.py 1 {files[m]} 2 {files[j]} ")


    with open(os.path.join("Run", f"Outputs{i}.py"), "a") as f:
        f.write("}")
    
    # finit.write(f"from .Outputs{i} import *\n")
    # listofoutputs.append((i, f"outputs{i}"))

# finit.write("outputs = {")

# for i in range(len(listofoutputs)):
#     finit.write(f"{listofoutputs[i][0]}: {listofoutputs[i][1]}, ")

# finit.write("}")

# finit.close()