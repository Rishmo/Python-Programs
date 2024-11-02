#Addition of 2 numbers using class and object
class Addition:
    def __init__(self,num1,num2):
        self.a=num1
        self.b=num2
    def display_reasult(self):
        result=self.a+self.b
        print(result)
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
a1=Addition(num1,num2) #creation of object
a1.display_result() #accessing member
