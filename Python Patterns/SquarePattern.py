#Square  pattern
n=int(input("Enter a number:")) #4
for i in range(1,n):
    for j in range(n):
        print("*",end=" ")
    print()

#Rectangle  pattern
n=int(input("Enter a number:"))
for i in range(n+1):
    for j in range(n):
        print("*",end=" ")
    print()
