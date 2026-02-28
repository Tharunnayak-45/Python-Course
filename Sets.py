# Sets are used to store multiple values in a single variable..
# Set is collection which is unordered,unchangeable",and unindexed..
# Set are written in curly braces {}...
set={1,2,3,4}
print(type(set)) # Type
print(set)
# Set are unorderedable but u can add and remove items ....
# Set do not allow duplicates values..
set={1,2,1,3,3,4}
print(set)

# Set-Data types
s1={"Hii","Hlo","Emc"}
s2={1,3,2,4}
s3={True,False,False,True}
print(s1)
print(s2)
print(s3)

# Access set items
# you cannot access items in a set by referring to an index are key but using loop using or in keyword
set={1,2,3,4,5}
for i in set:
    print(i)

# Check 3 is present in the set..
print(3 in set)
print(6 not in set)

#Add set items
set1={"CSE","IT","ECE","EEE"}
set1.add("AI")
print(set1)

#Update add sets
set2={"Java","CS","BEE","NLP","ML"}
set1.update(set2)
print(set1)

#remove set-items
set1={"CSE","IT","ECE","EEE"}
set1.remove("IT")
print(set1)

set1={"CSE","IT","ECE","EEE"}
set1.discard("ECE")
print(set1)

# Join-sets
# there are sevaral methods two join the sets in python....
# The Union() and Update() method joins all the items from both sets..
set1={1,2,3,4,5}
set2={"red","blue","green"}
set3=set1.union(set2)
print(set3)

# | operator also using two join the sets....
set1={1,2,3,4,5}
set2={"red","blue","green"}
set3=set1 | set2
print(set3)

# Multiple Sets also join in set...
set1={1,2,3,4,5}
set2={"red","blue","green"}
set3={"Tharun","Nithin","Rekya","Rukka"}
my_set=set3.union(set1,set2)
print(my_set)

#join a set and a a tuple
x={1,2,3,4}
y=("a","b","c")
z=x.union(y)
print(z)

#Intersection  keeps ONLY duplicates items...
set1={"apple","wipro","coznigant"}
set2={"wipro","accenture","factset"}
s=set1.intersection(set2)
print(s)

# You can use instead of & operator....
set1={"apple","wipro","coznigant"}
set2={"coznigant","accenture","factset","apple"}
s=set1 & set2
print(s)

# Difference() method will return a new set will contain the first set that are not presented in other set
s1={1,2,3}
s2={2,5,6}
s3=s1.difference(s2)
print(s3)

s1={1,4,3}
s2={2,3,6}
s3=s2 - s1
print(s3)
#systematic difference method will keep the only elements that are not in two sets..
s1={1,2,3}
s2={2,5,6}
s3=s1.symmetric_difference(s2)
print(s3)

s1={1,4,3}
s2={2,3,6}
s3=s2 ^ s1
print(s3)

# frozenset is a immutable version of set.
x=frozenset({1,2,3})
print(x)
print(type(x))

#Set Methods
set1={"john","sid","sim"}
set2={"hii","hlo","hoo","john"} # We should add the john in other set it will retuens False...
s=set1.isdisjoint(set2) #isdisjoint returns true if no items in set x is present set y...
print(s)

set1={"john","sid","sim","hii","hlo","hoo"}
set2={"hii","hlo","hoo"}
s=set1.issuperset(set2) #issuperset returns true if all items in set x is present set y...
print(s)
