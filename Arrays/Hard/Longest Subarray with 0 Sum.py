"""
****************
Better Approach
****************
1. Initialize a variable maxLen for storing maximum length
2. Iterate over the outer array i from 0 -> n
3. Initialize s = 0 after each iteration of outer loop
4. Iterate over the inner array j from i -> n
5. Check if sum == 0, if it is store maximum length in maxLen variable
6. Repeat and return maxLen

TC : O(n^2)
SC : O(1)
"""


def longestSubarray(arr, n):

    maxLen = 0
    for i in range(n):
        s = 0
        for j in range(i,n):
            s += arr[j]
            if s == 0:
                maxLen = max(maxLen, j - i + 1)

    return maxLen


"""
*****************
Optimal Approach 
*****************
1. Initialize two variables maxLen and prefixSum with 0.
2. Initialize a dictionary mapp to store prefixSum and index.
3. Traverse through the array and add current num to prefixSum.
4. Check if
    - prefixSum == 0 then increase maxLen to --> i + 1
    - prefixSum not in mapp, add to it
    - prefixSum in map --> update maxLen to (i - mapp[prefixSum]) which is current index 
        minus the prefixSum index in mapp
5. Return maxLen

TC : O(n log n)
SC : O(n) --> Store prefixSum and Index
"""


def longestSubarray(arr, n):

    prefixSum = 0
    maxLen = 0
    mapp = dict()

    for i in range(n):

        prefixSum += arr[i]

        if prefixSum == 0:
            maxLen = max(maxLen, i + 1)

        if prefixSum not in mapp:
            mapp[prefixSum] = i
        else:
            maxLen = max(maxLen, i - mapp[prefixSum])

    return maxLen


# Input to Code
arr = [15, -2, 2, -8, 1, 7, 10, 23]
n = len(arr)
print(longestSubarray(arr,n))
