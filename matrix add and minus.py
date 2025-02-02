matrixA = [[1,2],[3,4]]
matrixB = [[5,6],[7,8]]
matrixC = [[0,0],[0,0]]
matrixD= [[0,0],[0,0]]


for i in range(2):
    for j in range(2):
        matrixC[i][j]=matrixA[i][j]+matrixB[i][j]
        matrixD[i][j]=matrixA[i][j]-matrixB[i][j]

for i in range(2):
    for j in range(2):
        print(matrixC[i][j], end=" ")
    print("\n")

for i in range(2):
    for j in range(2):
        print(matrixD[i][j], end=" ")
    print("\n")