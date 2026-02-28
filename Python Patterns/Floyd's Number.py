n=int(input("Enter a number of rows:"))
n1=1
for i in range(1,n+1):
    for j in range(i):
        print(n1,"",end="")
        n1=n1+1
    print()

