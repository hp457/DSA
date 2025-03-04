"""
************
Optimal Code
********************************************************************************
1. We're using four pointers in the code left, right, top, bottom
2. Initially pointing to
    left -> [0,0]
    right -> [0,n-1] #Column length
    top -> [0,0]
    bottom -> [n-1,0] # Row length

3. Traverse mode would be
    left -> right --> update top to next once traversed
    top -> bottom --> update right to prev once traversed
    right -> left --> update bottom to prev once traversed
    bottom -> top --> update left to next once traversed

4. Run the same until all four points meet at the same point and break it
5. Also, cover the edge case in case of single row in the matrix.

********************************************************************************
"""

def spiralOrder(matrix):

    rows = len(matrix)
    columns = len(matrix[0])
    res = list()
    left = 0
    right = columns - 1
    top = 0
    bottom = rows - 1

    while left <= right and top <= bottom:

        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

    return res

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))
