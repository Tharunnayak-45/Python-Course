n=int(input("Enter a number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

#n=int(input("Enter a number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(1,n+1):
    for j in range(1,i+1):
        if (n-i)%2==0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()
        
