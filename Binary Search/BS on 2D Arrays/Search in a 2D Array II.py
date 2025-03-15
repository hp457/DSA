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

def searchMatrix(matrix, target):

    R = len(matrix)
    C = len(matrix[0])

    for row in range(R):

        for col in range(C):
            if matrix[row][col] == target:
                return True

    return False

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

TC : O(m * log2n)
SC : O(1)
**********************************************
"""

def searchMatrix(matrix, target):

    R = len(matrix)
    C = len(matrix[0])

    def ifTargetFound(arr, low, high):

        # Check if target between or in range, then search else return False
        if arr[low] <= target <= arr[high]:

            while low <= high:

                mid = (low + high) // 2

                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
        else:
            return False

    #Iterate over each sub array and pass it to ifTargetFound to check if is available or not.
    for i in range(R):

        if ifTargetFound(matrix[i], 0, C-1):
            return True

    return False


"""
**************
Optimal Approach
**********************************************
1. Start at the top-right corner of the matrix (i.e., the element in the first row and last column).
     We will call this element current.
2. Compare current with the target value target. If current is equal to target, 
    return true since we have found the target in the matrix.
3. If current is greater than target, we can eliminate the entire last column 
    (i.e., all elements in the last column are greater than current and therefore 
    greater than target). Move one column to the left to consider the next element in that row.
     We will call this new element current.
4. If current is less than target, we can eliminate the entire first row 
    (i.e., all elements in the first row are less than current and therefore less 
    than target). Move one row down to consider the next element in that column.
     We will call this new element current.
5. Repeat steps 2-4 until current is equal to target or we reach the end of the matrix.
6. If we reach the end of the matrix without finding the target, return false. 

TC : O(m+n)
SC : O(1)
**********************************************
"""


def searchMatrix(matrix, target):

    R = len(matrix)
    C = len(matrix[0])
    r = 0
    c = C - 1

    while r < R and c > -1:

        if matrix[r][c] == target:
            return True
        elif matrix[r][c] > target:
            c -= 1
        else:
            r += 1

    return False

# Input
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 3
print(searchMatrix(matrix, target))