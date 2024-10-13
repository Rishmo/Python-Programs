# Factorial of a number.

num = int(input("Enter a number: "))
fact = 1
if num < 0:
   print("Please enter positive integer value")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       fact = fact*i
   print("The factorial of",num,"is",fact)
