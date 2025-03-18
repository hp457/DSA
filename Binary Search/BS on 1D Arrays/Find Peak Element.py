"""
**************
Brute Approach
**********************************************
1. Iterate through the entire array.
2. Initialize two variables left and right with bool values initially True.
3. Now check if the previous number is greater than current set the left variable to False.
4. Similarly, if the current number is greater than forward set the right to False.
5. If both are true, means we got peak element and return it.

TC : O(n)
SC : O(1)
**********************************************
"""

def peakElement(nums, n):

    for i in range(n):

        left = True
        right = True

        if i > 0 and nums[i - 1] > nums[i]:
            left = False

        if i < n - 1 and nums[i] < nums[i + 1]:
            right = False

        if left and right:
            return i


"""
**************
Optimal Approach
**********************************************
1. The same BS approach will be followed
2. Initially keep the pointer low = 1 and high = n-2 of array. Because of the array is 
    entirely sorted in increasing/decreasing order than the first element or last element
    would be the peak element, so will handle that condition in code itself.
3. If there is one element return the index, also check the condition where index-0 is greater
    than index-1 then return 0 because on the left we're checking with -infinity.
    Same goes to n-1 if it is greater than n-2 then return n-1, because on the right we have
    infinity.
4. Calculate the mid element using (low + high) // 2
5. While loop till low <= high
6. Check if mid-1 < mid and mid > mid + 1, return it.
    If mid-1 < mid, then go to right half else left half.
7. There will be at least one peak element, and it will get returned.

TC : O(logN)
SC : O(1)
**********************************************
"""

def peakElement(nums, n):

    low = 1
    high = n - 2

    if n == 1:
        return 0

    if nums[0] > nums[1]:
        return 0

    if nums[n - 1] > nums[n - 2]:
        return n - 1

    while low <= high:

        mid = (low + high) // 2

        if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
            return mid
        elif nums[mid - 1] < nums[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Input
nums = [1,2,3,1]
n = len(nums)
print(peakElement(nums, n))



