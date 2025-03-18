"""
**************
Brute Approach
**********************************************
1. Iterate through the matrix and store each element in the new resultant array.
2. Now, sort the matrix
3. Return the middle index of the final array

TC : O(m*n + (m*n)log(m*n))
SC : O(m*n)
**********************************************
"""

def matrixMedian(mat):

    m = len(mat)
    n = len(mat[0])
    res = list()

    for sub_array in mat:
        for ele in sub_array:
            res.append(ele)

    res.sort()

    return res[(m * n) // 2]


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

    pass

# Input
mat = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
print(matrixMedian(mat))