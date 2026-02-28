n=int(input("Enter a number:"))
ch=65
for i in range(1,n+1):
    for j in range(i):
        print(chr(ch),end=" ")
        ch=ch+1
    print()

#Inverted AlphabetPattern........

n=int(input("Enter a number of rows:"))
ch=65
for i in range(n,0,-1):
    for j in range(i):
        print(chr(ch),end=" ")
        ch=ch+1
    print()
