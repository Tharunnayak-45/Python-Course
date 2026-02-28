n=int(input("Enter a number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        if (n-i-1)%2==0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()

#Inverted.....
n=int(input("Enter a number:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        if (n-i-1)%2==0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()

# BinaryPattern1................
n = int(input("Enter a number:"))
for i in range(1, n+1):
    for j in range(1, i+1):
        if (n - i - 1) % 2 == 0:
            print(0, end=" ") #u need to space u have to space in end=" "
        else:
            print(1, end=" ")
    print()
