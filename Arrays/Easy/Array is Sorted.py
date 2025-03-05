"""
********************************************************************************
1. Iterate from index 1 to n and return True if in sorted order else False
********************************************************************************
"""

def isSorted(arr,n):

    for i in range(1,n):
        if arr[i] < arr[i-1]:
            return False

    return True

arr = [1,2,2,3,4]
n = len(arr)
print(isSorted(arr,n))

