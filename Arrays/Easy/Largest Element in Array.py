"""
**************
Brute Approach
**********************************************
Sort the array and return (n-1)th element

TC : O(N log N)
SC : O(1)
**********************************************
"""

def largestElement(arr):

    arr.sort()
    n = len(arr)
    return arr[n-1]

"""
****************
Optimal Approach
********************************************************
Iterate through the array and update the largest element

TC : O(N)
SC : O(1)
********************************************************
"""

def largestElement(arr):

    largest = arr[0]
    n = len(arr)

    for i in range(n):
        if arr[i] >= largest:
            largest = arr[i]

    return largest

# Input
arr = [100, 8, 7, 56, 90]
print(largestElement(arr))