import numpy as np

matrixA = []
for i in open("input/matrixA.txt"):
    row = [int(x) for x in i.split(",")]
    matrixA.append(row)

matrixB = []
for j in open("input/matrixB.txt"):
    row = [int(x) for x in j.split(",")]
    matrixB.append(row)

matrixA = np.array(matrixA)
matrixB = np.array(matrixB)

ans = matrixA.dot(matrixB)
ans.sort(axis=1)

np.savetxt("output/HW00_01.txt", ans, fmt="%d", delimiter="\r\n")