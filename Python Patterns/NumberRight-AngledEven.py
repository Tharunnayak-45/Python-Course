n=int(input("Enter the number:"))
t=2
for i in range(1,n+1):
    for j in range(i):
        print(t,"",end="")
        t+=2
    print()