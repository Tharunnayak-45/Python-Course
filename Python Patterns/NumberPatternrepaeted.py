n=int(input("Enter a row:"))
for i in range(1,n+1):
    
    print(str(i)*i) #str(i) * i repeats the string i->i

#Inverted...
for i in range(n,0,-1):
    print(str(i)*i)
