import Run as ops

csvout = []
fingerprintvector = {}

for j in range(00, 2600, 100):
    fingerprintvector[(j, j + 100)] = []

for x in ops.outputs:
    out = ops.outputs[x]
    for i in out:
        finger = out[i]["Fingerprint1Len"] + out[i]["Fingerprint2Len"]
        code = out[i]["Code1Len"] + out[i]["Code2Len"]
        if out[i]["Plaintext Similarity"] > 0:
            savedata = {"err": abs(out[i]["Plaintext Similarity"] - out[i]["Secure Similarity"])/out[i]["Plaintext Similarity"], 
                        "time": out[i]["Total runtime - "],
                        "fing": finger,
                        "code": code,
                        "prp": (out[i][0][8][1] + out[i][1][8][1] + out[i][2][8][1])/3 + (out[i][1][11][1] + out[i][2][11][1])/2,
                        "shuffle": (out[i][0][11][1] + out[i][1][14][1] + out[i][2][14][1])/3 + (out[i][0][14][1] + out[i][1][17][1] + out[i][2][17][1])/2,
                        "rec": (out[i][0][17][1] + out[i][1][20][1] + out[i][2][20][1])/3,
                        "out": (out[i][0][20][1] + out[i][1][23][1] + out[i][2][23][1])/3,
                        }
        else:
            savedata = {"err": abs(out[i]["Plaintext Similarity"] - out[i]["Secure Similarity"]), 
                        "time": out[i]["Total runtime - "],
                        "fing": finger,
                        "code": code,
                        "prp": (out[i][0][8][1] + out[i][1][8][1] + out[i][2][8][1])/3 + (out[i][1][11][1] + out[i][2][11][1])/2,
                        "shuffle": (out[i][0][11][1] + out[i][1][14][1] + out[i][2][14][1])/3 + (out[i][0][14][1] + out[i][1][17][1] + out[i][2][17][1])/2,
                        "rec": (out[i][0][17][1] + out[i][1][20][1] + out[i][2][20][1])/3,
                        "out": (out[i][0][20][1] + out[i][1][23][1] + out[i][2][23][1])/3,
                        }
            
        x1 = int(finger/100)*100
        if savedata["out"] < 7.1:
            fingerprintvector[(x1, x1+100)].append(savedata)
            # csvout.append([savedata["time"], finger])

for x in fingerprintvector:
    prints = {
    "prp" : 0,
    "shuffle" : 0,
    "rec" : 0,
    "out" : 0,
    "time" : 0,
    "fing" : 0,
    "err" : 0,
    "code" : 0,
    }
    count = 0
    for j in fingerprintvector[x]:
        for k in j:
            prints[k] += j[k]
        count += 1
    for m in prints:
        prints[m] /= count
    prints["err"] *= 100
    csvout.append([prints["time"], prints["fing"]])
    y = f"    ${x[0]}-{x[1]}$ & ${round(prints['time'], 2)}$ & ${round(prints['prp'], 2)}$ & ${round(prints['shuffle'], 2)}$ & ${round(prints['rec'], 2)}$ & ${round(prints['out'], 2)}$ & ${round(prints['err']*10**6, 2)} \\times " + "10^{-6} $ \\\\ \hline"
    print(y)

with open("TimefingerComparison.csv", "w") as f:
    f.write("Fingerprintlen,time\n")
    for i in range(len(csvout)):
        f.write(f"{csvout[i][0]}, {csvout[i][1]}\n")

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

csv = pd.read_csv("TimefingerComparison.csv")
# print(csv.columns)
theta = np.polyfit(csv["time"], csv["Fingerprintlen"], 1)
y_line = theta[1] + theta[0] * csv["time"]
plt.scatter(csv["time"], csv["Fingerprintlen"], s=1, c="black" )
plt.plot(csv["time"], y_line, "black", linewidth=0.7)
plt.xlabel("Combined fingerprint length")
plt.ylabel("Run time in seconds")
plt.show()