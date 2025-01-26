matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
#to print rows
print(len(matrix))
#to print columns
print(len(matrix[0]))
#access an element from the 2D list
print(matrix[1][2])
for i in range(3):
    for j in range(3):
        print(matrix[i][j], end=" ")
    print("\n")