import sys

def menu():
    print("\nMenu:")
    print("1. See all the names in the list")
    print("2. Add a name to the list")
    print("3. Remove a name from the list")
    print("4. Change a name in the list")
    print("5. Exit")

names = ["Anjali", "Aryan", "Immanuel"]

c=int(input("Choose from the numbers 1-5 "))
if c==1:
    print(names)
elif c==2:
    a=input("Which name do you want to add? ")
    names.append(a)
elif c==3:
    r=input("Which name would you like to remove? ")
    names.remove(r)
elif c==4:
    ch=input("Which name would you like to change? ")
    upd=input("To what would you like to change the name? ")
    ind=0
    for i in names:
        if i==ch:
            names[ind]=upd
        else:
            ind+=1
elif c==5:
    sys.exit()
