"""
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Largest: ", max(a, b,c))
"""
#largest = max(a, b, c)
#print("Largest : ",largest) #or print("Largest: ", max(a, b,c))'''
"""
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

print("Largest: ",max(a, b, c))
"""

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a>=b and a>=c :
    print("Largest number is: ",a)
elif b>=a and b>=c :
    print("Largest number is: ",b)
else:
    print("Largest number is : ", c)
    