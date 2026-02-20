#Take input from the user and convert it to integer
num = int(input("Enter a number: "))

#Factorial is not defined for negative numbers
if num < 0:
    print("Factorial is not defined for negative numbers.")

else:
    #Initialize factorial variable to 1
    #we start with 1 because multiplying by 1 does not change the result
    factorial = 1

    #Loop From 1 to num (inclusive)
    #range(1, num + 1) generate numbers: 1, 2, 3, ...,  num

    for i in range(1, num + 1):
        #multiply current value of factorial by i
        factorial  = factorial * i

#print the final result 
print("Factorial of", num, "is", factorial)
  


