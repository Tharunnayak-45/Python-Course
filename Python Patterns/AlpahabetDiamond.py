n=int(input("Enter a number:"))
ch=65
for i in range(1,n+1):
    print(" "*(n-i)+chr(ch+i-1)*(2*i-1))
for i in range(n-1,0,-1):
    print(" "*(n-i)+chr(ch+i-1)*(2*i-1))
