"""
**************
Brute Approach
************************************************************
1. Store the values till D places into a temporary array
2. Iterate through D->n then place each ele at i index in the original array
3. Add temp array to the end of original array

TC : O(d) + O(n-d) + O(d) --> O(n+d)
SC : O(d)
**********************************************
"""

def leftRotateDPlaces(arr,n,d):

    temp = list()
    d = d % n

    for i in range(d):
        temp.append(arr[i])

    for i in range(d,n):
        arr[i-d] = arr[i]

    for i in range(n-d,n):
        arr[i] = temp[i-(n-d)]

    return arr

"""
**************
Brute Approach
************************************************************
1. Reverse the entire array
2. Reverse the element till D places
3. Reverse the elements from d->n places

TC : O(n) + O(n-d) + O(d) --> O(2n)
SC : O(1)
**********************************************
"""

def leftRotateDPlaces(arr,n,d):

    d = d % n

    arr.reverse()
    arr[:d] = reversed(arr[:d])
    arr[d:n] = reversed(arr[d:n])

    return arr



# Input
arr = [100, 8, 7, 56, 90]
n = len(arr)
d = 2
print(leftRotateDPlaces(arr,n,d))