#While lop we can execute set of stmts as long as condition becomes True...
#Starts with i=1
i=1 #a variable i is created and given the value i
while i<6: #the while loop runs as long as the condition is True.
    print(i) #print the i value
    i+=1 #increase i by 1 after each loop(same as=i=i+1)
# print("loop stops.")

i=1
while i<10:
    print("I love python🐍!")
    i=i+1

#Multiplication table using while loop
n=int(input("Enter a number:"))
i=1
while i<=10:
    print(n,"x",i,"=",n*i)
    i=i+1
print("loop finished.")

count=1
while count<5:
    print("I am inside a while loop.")
    print("Looping is intresting")
    count =count+1
