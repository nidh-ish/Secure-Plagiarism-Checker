# from main import *
# from Outputs import *
import Run as ops
import os

# print(ops.outputs)


for x in ops.outputs:

    avgerror = 0
    avgfilesize = 0
    avgfingsize = 0

    out = ops.outputs[x]

    l0 = {}
    l1 = {}
    l2 = {}

    for m in out[[x for x in out.keys()][0]][0]:
        l0[m[0]] = 0
    for m in out[[x for x in out.keys()][0]][1]:
        l1[m[0]] = 0
    for m in out[[x for x in out.keys()][0]][2]:
        l2[m[0]] = 0

    # print(out["o2y1x"][1][0][0])
    count = 0
    for i in out:
        for j in range(len(out[i][0])):
            l0[out[i][0][j][0]] += out[i][0][j][1]
        for j in range(len(out[i][1])):
            try:
                l1[out[i][1][j][0]] += out[i][1][j][1]
                l2[out[i][2][j][0]] += out[i][2][j][1]
            except:
                print(len(out[i][1]), len(out[i][2]), j, i)
        avgerror += abs(out[i]["Plaintext Similarity"] - out[i]["Secure Similarity"])
        avgfilesize += out[i]["Code1Len"] + out[i]["Code2Len"]
        avgfingsize += out[i]["Fingerprint1Len"] + out[i]["Fingerprint2Len"]
        count += 1

    # print(l0)
    # print(l1)
    # print(l2)

    # averages = {}

    for i in l0:
        l0[i] /= count
    for i in l0:
        l1[i] /= count
        l2[i] /= count

    avgerror /= count
    avgfilesize /= count
    avgfingsize /= count
    # print(l0)
    # print(l1)
    # print(l2)

    with open(os.path.join("Run", f"averageoutput{x}.txt"), "w") as f:
        f.write("0: ",)
        for i in l0:
            f.write(f"{i}: {l0[i]}, ")
        f.write("\n1: ",)
        for i in l1:
            f.write(f"{i}: {l1[i]}, ")
        f.write("\n2: ",)
        for i in l2:
            f.write(f"{i}: {l2[i]}, ")
        f.write(f"\nAverage error: {avgerror}")
        f.write(f"\nAverage Code Length: {avgfilesize}")
        f.write(f"\nAverage Fingerprint Length: {avgfingsize}")