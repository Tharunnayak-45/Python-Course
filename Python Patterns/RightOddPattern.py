n=int(input("Enter the row size:"))
for i in range(1,n+1): #Outer Loops for rows
    for j in range(n-1): # Inner Loops for spaces
        print("",end=" ")
    for k in range(1,2*i): # Inner loops for stars...
        print("*",end=" ")
    print()
#Inverted.......
n=int(input("Enter the row size:"))
for i in range(n,0,-1):
    for j in range(n-1):
        print("",end=" ")
    for k in range(1,2*i):
        print("*",end=" ")
    print()