n=int(input("Enter a number:"))
n1=2*n-1
for i in range(n1):
    for j in range(n1):
        if i==0 or j==0 or i==n1-1 or j==n1-1:
            print(3,end=" ")
        elif i==1 or j==1 or i==n1-2 or j==n1-2:
            print(2,end=" ")
        else:
            print(1,end=" ")
    print()

n = int(input("Enter a number:"))
n1 = 2 * n - 1
for i in range(n1):
    for j in range(n1):
        if i == 0 or j == 0 or i == n1 - 1 or j == n1 - 1:
            print(3, end=" ")
        elif i == 1 or j == 1 or i == n1 - 2 or j == n1 - 2:
            print(2, end=" ")
        elif i== 2 or j==2 or i==n1-3 or j==n1-3:
            print(1,end=" ")
        elif i == 3 or j == 3 or i == n1 - 4 or j == n1 - 4:
            print(0, end=" ")
        
        else:
            print(1, end=" ")
    print()
