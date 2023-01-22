"""
Python script that finds the middle of a 2D point cloud
"""

import math
import numpy as np

# Create some dummy data
x = np.array([1.0, 2.3, 4.5, 6.3, 8.2, 9.8, 10.1, 12.3, 14.9, 15.2])
y = np.array([2.2, 4.6, 5.0, 7.1, 8.6, 10.2, 12.6, 13.0, 15.2, 16.7])

# Calculate the mean of x and y
mean_x = np.mean(x)
mean_y = np.mean(y)

# Print the result
print("The middle of the point cloud is ({:.2f}, {:.2f})".format(mean_x, mean_y))