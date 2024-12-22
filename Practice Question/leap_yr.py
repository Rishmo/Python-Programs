n= int(input("Enter number: "))

if((n%4==0) and (n%100 != 0) or (n%400 == 0)):
    print(f"{n} is Leap year")
else:
    print(f"{n} is not Leap Year")