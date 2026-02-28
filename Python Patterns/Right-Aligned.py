#Right-aligned
n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)        #Here we remove the star spaces
#Shadow of Right-aligned
n=int(input("Enter a number:"))
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*i) #Here also same as space we remove