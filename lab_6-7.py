# Ask the user to input 3 numeric values
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

# Construct a list of the 3 input values in the order that the user gave them
num_list = [num1, num2, num3]

# Display a list with each of the values as integers that have been doubled
doubled_list = [num*2 for num in num_list]
print(doubled_list)