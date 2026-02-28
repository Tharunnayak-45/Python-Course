n=int(input("Enter a number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        if j==i or j==1 or i==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#Inverted.......
n=int(input("Enter a number:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        if j==i or j==1 or i==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

