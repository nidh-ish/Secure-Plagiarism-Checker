import os
import random



lengths = {}

for i in range(0, 250, 10):
    x = i, i+10
    lengths[x] = []

# for i in onlyfiles:
#     with open(i, "r") as f:
#         x = len(f.readlines())

#         x1 = x - x%10
#         lengths[(x1, x1+10)].append(i)


# for j in lengths:
#     if len(lengths[j]) > 0:
#         print(lengths[j][0])

with open("Combinedfile.py", "r") as f1:
    m = f1.readlines()
    mind = 0
    for x in lengths:
        print("inside", len(m))
        filesinx = [os.path.join(f"OriginalFiles", f"Test{x[0]}_{x[1]}", f) for f in os.listdir(os.path.join("OriginalFiles", f"Test{x[0]}_{x[1]}")) if os.path.isfile(os.path.join("OriginalFiles", f"Test{x[0]}_{x[1]}", f))]
        j = len(filesinx)
        while(j < 20):
            f0 = open(os.path.join(f"OriginalFiles", f"Test{x[0]}_{x[1]}", f"Cop{j}.py"), "w")
            l = x[0] + random.randint(1, 8)
            print(mind, l, x)
            while not (ord(m[mind][0]) >= ord("a") and ord(m[mind][0]) <= ord("z") or ord(m[mind][0]) >= ord("A") and ord(m[mind][0]) <= ord("Z")) :
                mind += 1
                if mind >= len(m):
                    mind = l
            print(m[mind][0])
            f0.writelines(m[mind:mind+l])
            mind += l
            if mind >= len(m):
                mind = l
            f0.close()
            j += 1