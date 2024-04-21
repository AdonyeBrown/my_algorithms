import bisect
import numpy as np

M = [
    [4, 3, 2, -1],
    [3, 2, 1, -1],
    [1, 1, -1, -2],
    [-1, -1, -2, -3]
]

matrix = np.array(M)
# A function to find the first negative number in a sorted array using binary search


def find_first_negative(arr):
    # Initialize low and high pointers
    # Loop until low and high cross each other
    # Find the middle index
    # If the middle element is negative, move the high pointer to the left
    # If the middle element is non-negative, move the low pointer to the right
    # Return the low pointer, which is the index of the first negative number
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < 0:
            high = mid - 1
        else:
            low = mid + 1
    return low

# A function to count the number of negative numbers in a matrix using binary search


def count_negative(matrix):
    # Initialize the count to zero
    # Loop over each row of the matrix
    # Find the index of the first negative number in the row
    # Add the number of negative numbers in the row to the count
    # Return the count
    cont = 0
    for row in matrix:
        index = find_first_negative(row)
        cont += len(row) - index
    return cont


# Test the code on an example matrix
# Use list comprehension to create a list of booleans indicating whether each number is negative
# Use the sum function to count the number of True values in the list
# Print the result

print(count_negative(matrix))
negatives = [num < 0 for grid in matrix for num in grid]
cout = sum(negatives)
print(cout)


# Import the bisect module

# A function to count the number of negative numbers in a matrix using binary search

def count_negative(matrix):
    # Use list comprehension to find the index of the first negative number in each row
    # Use bisect.bisect_left to find the insertion point of 0 in the sorted row
    # Subtract the index from the length of the row to get the number of negative numbers
    # Sum up the results for all rows
    return sum(len(row) - bisect.bisect_left(row, 0) for row in matrix)


# Test the code on an example matrix
print(count_negative(matrix))
