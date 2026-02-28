#Conditional Statements in python programs to make decision amd execute different blocks...
#Conditional Statememt are in python is if,if elif,else....
#if statement execute only block of code only it will give us True...
x=5
if x>4:
    print("x is greater than 5")

#if else statement  provides alternatives the block of code to execute if condition is evaluates False..
n=4
if n%2==0:
    print("Even")
else:
    print("Odd")

#if-elif-else  statement allows for checking multiple conditions...
#Here I should take a student marks
marks=95
if(marks>=95):
    print("A grade")
elif(marks>=80):
    print("B grade")
elif(marks>=75):
    print("C grade")
else:
    print("Fail")

#else statement execute only the code is false statement in given condition...
a=2
if(a>4):
    print("if statement is executed")
else:
    print("else statement is executed")

#Program check the eligiblity to vote..
age=int(input("Enter an age number:"))
if age>=18:
    print("you r eligible to vote")
else:
    print("you r  not eligible to vote")

#Nested if-else statement be executed the each other to handle more complex decison making expression...
num=int(input("Enter a num:"))
if num>0:
    if num%2==0:
        print("The given number is divided")
    else:
        print("The given number is not divided")
else:
    print("Null")