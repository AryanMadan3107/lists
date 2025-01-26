r=int(input("How many rows would you like to add to the matrix? "))
c=int(input("How many columns would you like to add to the matrix? "))
matrix=[]
for i in range(r):
    temp = []
    for j in range(c):
        e=int(input("enter a number: "))
        temp.append(e)
    matrix.append(temp)

for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=" ")
    print("\n")