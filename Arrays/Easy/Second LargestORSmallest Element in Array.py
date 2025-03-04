import sys
"""
**************
Brute Approach
**********************************************
1. Sort the array return the (n-1)th element which would be the largest
2. Run a while loop till we find second largest and it is not equal to largest

TC : O(N * log N) + O(N)
SC : O(1)
**********************************************
"""

def secondLargestElement(arr,n):

    arr.sort()
    slargest = -1
    largest = arr[n-1]

    for i in range(n-2, -1, -1):
        if arr[i] != largest:
            slargest = arr[i]
            break

    return [largest, slargest]



"""
**************
Better Approach
**********************************************
1. Two loops, one for finding largest and another for finding second largest

TC : O(N) + O(N) --> O(2N)
SC : O(1)
**********************************************
"""

def secondLargestElement(arr,n):

    largest = -1
    slargest = -1

    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]

    for i in range(n):
        if arr[i] > slargest and arr[i] != largest:
            slargest = arr[i]

    return [largest, slargest]


"""
**************
Optimal Approach
**********************************************
1. Initially largest would be the first element and sslargest would be -1
2. If we found a element greater than largest so the slargest is going to be largest and
largest would be updated. Also, check if curr element is lesser than largest and greater than
slargest and update it.

TC : O(N)
SC : O(1)
**********************************************
"""

def secondLargest(arr, n):

    largest = arr[0]
    slargest = -1

    for i in range(1,n):
        if arr[i] > largest:
            slargest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > slargest:
            slargest = arr[i]

    return [largest, slargest]


def secondSmallest(arr, n):

    smallest = arr[0]
    ssmallest = sys.maxsize

    for i in range(1,n):
        if arr[i] < smallest:
            ssmallest = smallest
            smallest = arr[i]
        elif arr[i] != smallest and arr[i] < ssmallest:
            ssmallest = arr[i]

    return [smallest, ssmallest]



# Input
arr = [100, 8, 7, 56, 90]
n = len(arr)