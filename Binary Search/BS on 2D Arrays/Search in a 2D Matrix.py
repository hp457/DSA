"""
**************
Brute Approach
**********************************************
1. Calculate R(rows) and C(columns) of the matrix
2. Iterate through each row and column and if it matches with target, return True else False

TC : O(m * n)
SC : O(1)
**********************************************
"""

# def searchMatrix(matrix, target):
#
#     R = len(matrix)
#     C = len(matrix[0])
#
#     for row in range(R):
#
#         for col in range(C):
#             if matrix[row][col] == target:
#                 return True
#
#     return False

"""
**************
Better Approach
**********************************************
1. The same BS approach will be followed
2. First iterate over each sub-array in the array and pass that sub array to a user defined
    function to check if target is found or not
3. Function takes argument as arr, low, high
4. Use the same binary search approach
5. Before performing BS, check if target is between arr[0] and arr[n-1], if not return False
    else go for BS
5. Calculate mid and check if it equals target, then return True
    -- if lesser than target : search right half
    -- if greater than target : search left half
6. Once all sub array processed, return True or False.

TC : O(m) + O(log2n)
SC : O(1)
**********************************************
"""

# def searchMatrix(matrix, target):
#
#     R = len(matrix)
#     C = len(matrix[0])
#
#     def ifTargetFound(arr, low, high):
#
#         # Check if target between or in range, then search else return False
#         if arr[low] <= target <= arr[high]:
#
#             while low <= high:
#
#                 mid = (low + high) // 2
#
#                 if arr[mid] == target:
#                     return True
#                 elif arr[mid] < target:
#                     low = mid + 1
#                 else:
#                     high = mid - 1
#         else:
#             return False
#
#     #Iterate over each sub array and pass it to ifTargetFound to check if is available or not.
#     for i in range(R):
#
#         if ifTargetFound(matrix[i], 0, C-1):
#             return True
#
#     return False


"""
**************
Optimal Approach
**********************************************
1. The same BS approach will be followed
2. Consider the whole 2D matrix as a 1D matrix and think the whole problem into that perspective
3. Now the calculate the 2D index of element in 1D use the following concept:
    - row = num // C
    - col = num // C
    Here C is the column length and num is the number in 2D Array
4. Now check if matrix[row][col] equals target, return if
    - if lesser than check right half else left half ( Increase left and right half the same
        as you work 1D array )
5. Return True if found else False 

TC : O(log2(m*n))
SC : O(1)
**********************************************
"""


def searchMatrix(matrix, target):

    R = len(matrix)
    C = len(matrix[0])
    low = 0
    high = (R * C) - 1

    while low <= high:

        mid = (low + high) // 2
        row = mid // C
        col = mid % C

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

# Input
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 100
print(searchMatrix(matrix, target))