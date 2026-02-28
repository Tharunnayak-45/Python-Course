#String in python are surronded by either ' '," ",""" """...
#Strings are sequence of characters.....
#Strings are immutable...can't be changed...
str="Hello Python"
str1="World"
str2=str+" "+str1
print(str)
# check the class of str
print(type(str))

#Access of String
s="Tharunnayak"
print(s[2])
print(s[1])
print(s[-1])
print(s[1:3])
print(s[1::2])

#String Operations len,concat,cpy,reverse...
print(len(str))
print(str[::-1])
print(str2)

#iterable strings
s=["Tharun","Rukka","Rekya","Nithin"]
for i in s:
    print(s) # end keyword string appended after the last value, default a newline.
