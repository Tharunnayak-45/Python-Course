#Strings methods they are differnt methods
str="Hello Hii"
print(str.capitalize()) #Upper case the first letter in this word...
print(str.casefold()) #All Upper case the first letters in this word...
print(str.title())
print(str.upper()) #Gives the all uppercase letters
print(str.lower()) #gives the all lowecases letters
print(str.find("e")) #finds the first occurence of the specified value
print(str.count("l")) #counts the number of occurence of the specified value
print(str.replace("H"," ")) #replace the character of given string
#islower() it gives the Boolean Value.
print(str.islower()) #False
print("H".islower()) #False
print("o".islower()) #True
#isdigit() if all the caharacters is digits
str1="12345"
str2="Tharun"
print(str1.isdigit()) #True
print(str2.isdigit()) #False