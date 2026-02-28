n=int(input("Enter a number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i)+str(i)*(2*i-1))

#Inverted....
# n=int(input("Enter a number of rows:"))
for i in range(n-1,0,-1):
    print(" "*(n-i)+str(i)*(2*i-1))
