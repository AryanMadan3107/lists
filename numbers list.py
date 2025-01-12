numbers=[]
even=[]
odd=[]
for i in range(1,51,1):
    numbers.append(i)
    if (i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)