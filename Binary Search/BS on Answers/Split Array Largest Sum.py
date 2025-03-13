"""
**************
Brute Approach
**********************************************
1. For an array what could be the minimum sum for a sub-array, definitely it is max of that
    array right, and what could be the maximum sum, sum of array
2. So, iterate over the range --> (max, sum + 1)
3. For each sum, calculate the number of subArrays can be formed from the array.
4. If it is lesser or equals k, return the sum

TC : O(sum(arr) - max(arr) + 1) * O(n)
SC : O(1)
**********************************************
"""

def splitArrayLargestSum(nums, n, k):

    maximumSum = max(nums)
    totalSum = sum(nums)

    for s in range(maximumSum, totalSum + 1):

        cnt = 1
        current_sum = 0

        for num in nums:
            if current_sum + num <= s:
                current_sum += num
            else:
                cnt += 1
                current_sum = num
                if cnt > k:
                    break

        if cnt <= k:
            return s


"""
**************
Optimal Approach
**********************************************
1. The same BS approach will be followed
2. Initially keep the pointer low = max(arr) and high = sum(arr) of array
3. Calculate the mid element using (low + high) // 2
4. While loop till low <= high
5. Now using a function, calculate if we can the mid/sum can create <= k subarrays
    - The same function used in brute approach.
    - Iterate through the array using the mid/sum and count subArrays
    - If they exceeds k return false else true
6. Once done return low ( Do it on a paper you would understand why low will be returned )

TC : O(n * log2(sum - max + 1))
SC : O(1)
**********************************************
"""

def splitArrayLargestSum(nums, n, k):

    low = max(nums)
    high = sum(nums)

    # Function to calculate how many subArray can be formed for that sum.
    def checkSubArrays(nums, mid, k):

        # Iterate through each page in pages array
        cnt = 1
        current_sum = 0

        for num in nums:
            if current_sum + num <= mid:
                current_sum += num
            else:
                cnt += 1
                current_sum = num
                if cnt > k:
                    return False

        if cnt <= k:
            return True

    # Perform BS on the range
    while low <= high:

        mid = (low + high) // 2

        # Calculate if the pages/books can be distributed to all students
        if checkSubArrays(nums, mid, k):
            high = mid - 1

        # Else on right side
        else:
            low = mid + 1

    return low

# Input
nums = [1,2,3,4,5]
n = len(nums)
k = 2
print(splitArrayLargestSum(nums, n, k))