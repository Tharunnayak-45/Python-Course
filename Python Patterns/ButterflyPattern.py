#ButterflyPattern
#print("*" * i + " " * (2 * (n - i)) + "*" * i)
#"* "*i stars for the left wing
# #2*(n - i) spaces in the middle
#"* "*i stars again for the right wing

n = int(input("Enter the number of rows: "))
# Upper half
for i in range(1, n+1):
    print("*"*i+" "*(2*(n-i))+"*"*i)

# Lower half
for i in range(n-1,0,-1): #Here n-1 is decrement by 1
    print("*"*i+" "*(2*(n-i))+"*"*i)