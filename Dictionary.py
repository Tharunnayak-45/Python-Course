# A dictionary is a collection of key-value pairs.declare like a set curly braceses...
# It is unordered, changeable (mutable), and does not allow duplicates.
# Keys must be unique and immutable like strings or numbers.
dict={"name":"Tharun",
    "age":19,
    "college":"VJIT"}
print(dict)
print(type(dict))

#Duplicates are not allowed..
dict={"color":"Yellow",
    "days":30,
    "flower":"Sunflower",
    "days":30}
print(dict)
print(len(dict))

#Access the dict....
my_dict={"fruits":["Grapes","Mango","Apple"],
        "price":50,"kg":3}
print(my_dict["price"])
print(my_dict["fruits"])

#Get-keys()
# Get a list of all keys
my_dict={"fruits":["Grapes","Mango","Apple"],
        "price":50,"kg":3}
x=my_dict.keys()
print(x)

#Change dictionary
d1={"car":"volvo",
    "model":"Suzuki",
    "year":2000}
d1["year"]=2020
print(d1)

#Adding a dict....
d={"car":"volvo",
    "model":"Suzuki",
    "year":2000}
d["color"]="black"
print(d)

#Remove Dictionary
dict={"name":"Tharun",
    "course":"CSE",
    "college":"VJIT",
    "Id":545,
    "percentage":8.4}
print(dict)
x=dict.pop("college")
x1=dict.pop("Id")
print(x)
print(x1)

#Loop Dictionary
dict1={"name":"Tharun",
    "course":"CSE",
    "college":"VJIT",
    "Id":545,
    "percentage":8.4}
for i in dict1:  # here print all the keys in the dictionary
    print(i)

for i in dict1:
    print(dict1[i]) # Here it will print the all the values

# Get key and values
dict1={"Name"":":"Tharun",
    "Course"":":"CSE",
    "College"":":"VJIT",
    "Id"":":545,
    "Percentage"":":8.4}
for x,y in dict1.items():
    print(x,y)

#Nested Dictionary
students={
    "student1":{
        "name":"tharun",
        "age":19,
        "marks":99,
},
    "student2":{
    "name":"Nithin",
    "age":17,
    "marks":100,
    }
}
print(students)

for x,y in students.items():
    print(x,y)

#Dictionary Methods....
my_dict = {
    "name": "Nicky",
    "age": 19,
    "city": "Hyderabad",
    "place":"Aramghar"
}
x=my_dict.get("age") #get method returns the specific key..
print(x)

x=my_dict.values() #values get all the values not keys
print(x)

x=my_dict.keys() #keys get all the keys....
print(x)

my_dict.clear() #remove all the items in a dict
print(my_dict)
