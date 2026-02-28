#Slicing is a sub part of String
#We have to find the indexes of the characters given string so we using slicing concept
#Slicing  concept we have to find the character  so we can use of square brackets []
str="Hello World"
print(str[0:2]) #He
print(str[1:6]) #ello
print(str[1::3]) #eood
print(str[::2]) #HloWrd
print(str[2::2]) #loWrd
print(str[0::6]) #H W
print(str[::])  #it will print given str
print(str[0::4])

#Negative Slicing starts from at the end.....
print(str[::-1])
print(str[-11:-7])
print(str[-1::-2])
print(str[-11::])
print(str[::])