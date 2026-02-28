#Operators are used to perform the opertaions and values different types of operators
#Arthimatic Operators that are +,-,*,/..
a=1
b=2
print(a+b) #Addition
print(a-b) #Subraction
print(a*b) #Multiplication
print(a/b) #Division
print(a%b) #Modulus #It will gives a remainder value..

#Assignment Operator that are Increment & Decrement values
x=2
x=x+10 #Increment the a=1+10=>11
print(x)
y=5
y=y-2
print(y) #Decrement the b=2-2=>0

#Comparison Operators that are >,<,==,<=,>=,!=... and we remaine one thing i.e operators gives a Boolean Values
print(a>b) #1>2 No that's why it will returns the False
print(a<b) #1<2 No that's why it will returns the True
print(a==b) #1==2 No that's why it will returns the False
print(a!=b) #1!=2 No that's why it will returns the True
print(a<=b) #1<=2 No that's why it will returns the True
print(a>=b) #1>=2 No that's why it will returns the False

#Logical Operators that are and,or,not......
a=30
b=20
print(a>b and b<a) #Returns True if both the statement is True
print(a<b or a>b)  #Returns True if one of the statement is True
print(not(a>b))  #Reverse the result i.e if statement is True it will give False

#Ternary Operator
#In python this also offers one-line condition expression...
marks=15
Student="Topper" if marks>=10 else "Loser"
print(Student)