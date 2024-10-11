#to check amstrong number

num = int(input("Enter a number to check amstrong number: "))
temp=num
sum=0
c=0
while(temp>0):
    r=num%10
    c=c+1
    temp=temp//10
temp=num
while temp>0:
    r=temp%10
    sum=sum+r**c
    temp=temp//10
      
if sum==num:
    print("Armstrong Number")
else:
    print("Not armstrong number")


