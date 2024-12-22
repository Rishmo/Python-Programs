def factorial(n):
    if n == 0:
        return 1
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

n= int(input("Enter a digit: "))
fact = factorial(n)
print(fact)