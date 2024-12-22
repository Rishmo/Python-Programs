# l=[1,3,5,7,8]
# sum=(sum(l))
# print(sum)

# Program to take a specified number of values for a list and print it

# Input: Number of values in the list
count = int(input("Enter the number of values you want in the list: "))

# Initialize an empty list
values = []

# Take values as input based on the count
print(f"Enter {count} values:")
for i in range(count):
    value = input(f"Enter value {i + 1}: ")
    values.append(value)

# Print the final list
print("The final list is:", values)



