#define a recursive function to calculate factorial
def factorial(n):
    #Base case:
    # If n is 0 or 1, factorial is 1
    if n == 0 or n == 1:
        return 1
    
    #Recursive case:
    #n! = n * (n-1)!
    return n * factorial (n-1)

#Take input from user
num = int(input("Enter a number: "))

#check for negative numbers
if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    result = factorial(num)
    print(f"factorial of {num} is {result}")