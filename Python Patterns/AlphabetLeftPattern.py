# LeftAlphabetPattern
n=int(input("Enter a number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+i),"",end="") #chr(64 + i)-means it prints the same letter on each line, based on the row number
    print()
#Reverse order........
n=int(input("Enter a number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(65+n-i),"",end="")
    print()

#Inverted........
n=int(input("Enter a number:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(64+i),"",end="")
    print()

#-----------------------------------------------------------------------
# Right-AngledAlphabetPattern...
# Instead of i we use j increment the A value constant...
n=int(input("Enter a number:"))
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+j),"",end="") #chr(65 + j) — so it prints increasing letters starting from A up to a limit
    print()

#Inverted Right-Angled Pattern
n=int(input("Enter a number:"))
for i in range(n,0,-1):
    for j in range(i):
        print(chr(65+j),"",end="")
    print()