from main import *
import os
lengths = {}

for i in range(0, 250, 10):
    x = i, i+10
    lengths[x] = []

listofoutputs = []

finit = open(os.path.join("Run", "__init__.py"), "w")
for x in lengths:
    i = x[0]
    with open(os.path.join("Run", f"Outputs{i}.py"), "w") as f:
        f.write(f"outputs{i} = {{\n")
    
    # files = listoffiles[i]
    files = [os.path.join(f"TestFiles", f"Test{x[0]}_{x[1]}", f) for f in os.listdir(os.path.join("TestFiles", f"Test{x[0]}_{x[1]}")) if os.path.isfile(os.path.join("TestFiles", f"Test{x[0]}_{x[1]}", f))]

    for m in range(len(files)):
        for j in range(m):
            os.system(f"python main.py 1 {files[m]} 2 {files[j]} >> " + os.path.join("Run", f"Outputs{i}.py"))


    with open(os.path.join("Run", f"Outputs{i}.py"), "a") as f:
        f.write("}")
    
    finit.write(f"from .Outputs{i} import *\n")
    listofoutputs.append((i, f"outputs{i}"))

finit.write("outputs = {")

for i in range(len(listofoutputs)):
    finit.write(f"{listofoutputs[i][0]}: {listofoutputs[i][1]}, ")

finit.write("}")

finit.close()