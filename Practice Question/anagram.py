num1= input("Enter first number: ")
num2= input("Enter second number:")

if(sorted(num1) == sorted(num2)):
    print("Numbers are anagram")
else:
    print("Numbers are not anagram")