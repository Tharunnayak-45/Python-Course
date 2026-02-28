n=int(input("Enter a number:"))
for i in range(0,n):
    for j in range(n):
        print(chr(65+i),"",end="")
    print()

#Inverted........
n=int(input("Enter a number:"))
for i in range(0,n):
    for j in range(n):
        print(chr(65+n-i),"",end="")
    print()


n=int(input("Enter a number:"))
for i in range(0,n):
    for j in range(n):
        print(chr(65+j),"",end="")
    print()
