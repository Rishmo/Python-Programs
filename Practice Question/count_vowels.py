str = input("Enter a string: ")
vowels = "aeiouAEIOU"
count =sum(1 for char in str if char in vowels)
print(count)