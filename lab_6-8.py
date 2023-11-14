# Ask the user to input 3 numeric values
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

# Construct a list of the 3 input values in the order that the user gave them
num_list = [num1, num2, num3]

# Display whether the numbers in the list are all even, all odd, or mixed
if all(num % 2 == 0 for num in num_list):
    print("even")
elif all(num % 2 == 1 for num in num_list):
    print("odd")
else:
    print("mixed")