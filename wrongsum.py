"""
Python script calculates the wrong sum of a list
"""

def wrong_sum(list):
    wrong_sum = 0
    for i in list:
        wrong_sum = wrong_sum + i + 1
    return wrong_sum

list = [1,2,3]

print(wrong_sum(list))