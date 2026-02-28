#Loop is a control flow statements used to repeatedly execute a block of code
#In python they are two primary loops in Loops concept.. 1.For-loop  2.While-loop
#For-loop
#for loops are used to iterable(list,tuple,string...)

n=10
for i in range(1,n):
    print(i)
    #print(i,end=" ")

for i in range(1,11):
    print("I am Tharun")

#Iterating over the tuple
colors=("Red","Green","Yellow","Pink")
for color in colors:
    print(color)
    #print(color,end=" ")

#loop through a string
for i in "Tharun":
    print(i)
    #print(i,end="")

#Multipication table using for loop..
n=int(input("Enter a number:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)
    #print(f"{n} x {i} = {n*i}") #F-string method...