#Lists are used to store multiple items in a single variable
#list are mutable Data structure...changeable values,Orderable,allow duplicates...
#Creating  a list
li=[1,2,3,4]
print(li)
print(type(li))

lst=(1,1.5,"True","Hello") # in tuples data structure we need to create the list also
print(list(lst))

#Acesssing of list
l=[1,2,3,4,5,6]
print(len(l))
print(l[0])
print(l[1:4])
print(l[::-1])
print(l[-6::-2])

#Change list items .. you can change the list items using index numbers
fruits=["apple","banana","mango"]
fruits[1]="cherry"
print(fruits)

#Change the range items.....
fruits=["apple","banana","mango","grapes","pine-apple"]
fruits[1:3]=["Strawberry","Guava"] #here the fruits are replace their particular ranges...
print(fruits)

#Add List items
car=["BMW","Ferari","Volvo"]
car.append("Suzuki") #append to add items at the end of the list so we use append items.....
print(car)
car.remove("Ferari") #remove method is aspecific itens we have to remove...
print(car)

#Loop lists
#For loop list
age=[12,15,16,17,19]
for i in age:
    print(i)

#While loop
age1=[20,21,23,25]
i=0
while i<len(age1):
    print(age1[i])
    i=i+1

#List Methods
lst=["red","green","yellow","blue"]
lst.append("brown") #append to add items at the end of the list so we use append items.....
print(lst)
lst.remove("green") #Removes the element at the specific position
print(lst)
x=lst.count("red") #Count methods number of times the value appear in a list..........
print(x)
x=lst.index("blue") #index method position of the yellow  color ......
print(x)
lst.reverse() #reverse the elments from a list
print(lst)
lst.sort() #sort all the elements in a ascending order....
print(lst)
lst.pop(1) #remove the element at the specific position.....
print(lst)
lst.clear() #remove all elements from a list
print(lst)
