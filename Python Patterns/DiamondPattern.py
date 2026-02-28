n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(" "*(n-i+1)+"* "*i)
for i in range(n,0,-1): #Here n-1 means decrement by 1 
    print(" "*(n-i+1)+"* "*i)