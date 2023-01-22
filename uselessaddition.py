"""
Python script adds two numbers together in a useless way
"""

# Get user input
num1 = input("Please enter a number: ")
num2 = input("Please enter a second number: ")

# Convert strings to integers
num1 = int(num1)
num2 = int(num2)

# Add the two numbers
total = num1 + num2

# Convert total back to a string
total = str(total)

# Reverse the string
total = total[::-1]

# Convert reversed string back to an integer
total = int(total)

# Print result
print("The answer is " + str(total))