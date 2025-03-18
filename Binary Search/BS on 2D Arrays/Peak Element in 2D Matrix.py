"""
**************
Optimal Approach
**********************************************
1. The same BS approach will be followed
2. Initially keep the pointer low = 0 and high = colLength-1 of array.
3. Now the idea behind this, calculate the maxElement across the column and get the row
    index.
4. Now take two variables left and right, and capture the values of nearby index, in that row.
5. If [rowIndex][mid] is lesser than left, means the element in on left side else right.

TC : O(m * logN)
SC : O(1)
**********************************************
"""

def peakElement(mat):

    rows = len(mat)
    cols = len(mat[0])
    low = 0
    high = cols - 1

    # Function to find max element in the mid column and return the index.
    def findColMaxElement(mat, rows, col):

        index = -1
        maxEle = -1
        for i in range(rows):
            if mat[i][col] > maxEle:
                index = i

        return index

    while low <= high:

        mid = (low + high) // 2
        rowMaxIndex = findColMaxElement(mat, rows, mid)

        # Now store left and right value of that row into below variables
        left = mat[rowMaxIndex][mid - 1] if mid - 1 >= 0 else -1
        right = mat[rowMaxIndex][mid + 1] if mid + 1 < cols else -1

        # Check if value is greater than both left and right return it.
        if mat[rowMaxIndex][mid] > left and mat[rowMaxIndex][mid] > right:
            return [rowMaxIndex, mid]
        # Check for left half
        elif mat[rowMaxIndex][mid] < left:
            high = mid - 1
        # Else right
        else:
            low = mid + 1

    return [-1, -1]

# Input
mat = [[10,20,15],[21,30,14],[7,16,32]]
print(peakElement(mat))