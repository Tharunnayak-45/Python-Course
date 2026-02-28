#PyramidPattern
n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))
#Inverted PyramidPattern
n=int(input("Enter a number:"))
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))