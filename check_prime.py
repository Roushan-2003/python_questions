#Function to check prime number
def is_prime(n):
    #Prime number are greater than 1
    if n <= 1:
        return False
    
    #Check divisibility from 2 to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        
    return True

#taking input from user
num = int(input("Enter a number: "))

if is_prime(num):
    print(num, " is a prime nunber")

else:
    print(num,"is Not a prime number")