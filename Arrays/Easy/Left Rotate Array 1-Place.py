"""
**************
Approach
**********************************************
1. Store the first index value in temp variable
2. Iterate through 1->n then place each ele at i-1 index
3. Add temp variable value to end of array

TC : O(n)
SC : O(1)
**********************************************
"""

def leftRotate(arr,n):

    temp = arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]

    arr[n-1] = temp

    return arr


# Input
arr = [100, 8, 7, 56, 90]
n = len(arr)
print(leftRotate(arr,n))