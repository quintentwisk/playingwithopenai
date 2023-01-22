"""
Python script that finds the number in a list that is closest to the average of the list
"""

 # Create a list
my_list = [5, 6, 3, 9, 9, 5, 7]

# Find the average of all numbers in the list
average = sum(my_list)/len(my_list)

# Find the closest number to the average
closest_number = min(my_list, key=lambda x:abs(x-average))

# Print the closest number
print(average)
print(closest_number)