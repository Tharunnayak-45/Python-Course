#NumberPattern
n=int(input("Enter a number size:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,"",end="")
        #print(i,"",end="")
    print()
#Inverted...
n=int(input("Enter a row number:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()