# Tuples are used to store multiples items in a single varaiable..
# A Tuple is a collection which is oderded whivh is can't changeable..
#Creating a tuple using open brackets....()
t=(1,2,3)
print(t)
print(type(t)) #type..
#Remember that using only one single , is also tuple
tup=("Hello",)
print(type(tup))

#Tuple items - Data Types
n=(1,"Hii",True,9.6)
print(n)
print(type(n))

#Accesing a tuple..
#Note that every first index starts from 0..
tup1=(1,2,3,"Tharun",True)
print(tup1[0])
print(tup1[1:4])
print(tup1[::2])
print(tup1[:3])
print(tup1[::-1])
print(tup1[-1:-3])
print(tup1[-1::-2])

#Ranges..using a specific index to print value items....
names=("Tharun","Nithin","Rekya","Rukka","Sindhu")
print(names[0:3])
print(names[0::4])

#Check if exits..
names=("Tharun","Nithin","Rekya","Rukka","Sindhu")
if "Tharun" in names:
    print("""Yes,"Tharun" is there in names tuple""")

#Updates the tuple..
#Once you create a tuple you can't change the tuple because of the tuples are immutable..
#You can covert the tuple to list
name=list(names)
name[4]="Amru & Gamli"
names=tuple(name)
print(names)

#Add items...
#They don't have a built in method..like append,remove...
# Covert into a list
x=("red","green","maroon","blue","orange")
y=list(x)
y.append("pink")
x=tuple(y)
print(x)
# Add tuple to tuple..
y=("brown",)
x += y
print(x)
# Remove the tuple items using remove method...
x=("red","green","maroon","blue","orange")
y=list(x)
y.remove("green")
x=tuple(y)
print(x)

#Tuple methods
t=(1,3,5,2,3,4,5,6,3,1,3,3)
x=t.count(3)
print(x)

# Loops through the tuples...
tup1=("Salaar","Rdx","Hii","Bahubali","Pushpa")
for i in tup1:
    print(i)

for i in range(len(tup1)):
    print(tup1[i],"",end="")

#While-loop
y=(1,2,3,4)
i=0
while i<len(y):
    print(i)
    i=i+1

# Join tuples
#Joining the tuples one or more two tuples... using + operator
tup1=("a","b","c")
tup2=(1,2,3)
print(tup1+tup2)