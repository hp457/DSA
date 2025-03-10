import math
"""
**************
Brute Approach
**********************************************
1. Take out the maximum value from the array.
2. Run a loop i from 1 -> maxELe + 1 calculated from above step
3. For each number, calculate maxDivSum over the entire array.
4. The moment the maxDivSum <= threshold, return the num

TC : O(max(array) * n)
SC : O(1)
**********************************************
"""

def smallestDiv(nums, threshold):

    n = len(nums)
    # Maximum divisors that can be possible
    maxEle = max(nums)

    for num in range(1, maxEle + 1):
        smallestDivSum = 0

        # Calculate divisor sum for the num ranging from 1 -> maxEle
        for j in range(n):
            smallestDivSum += math.ceil(nums[j] / num)

        # If we found the minimum div sum return it.
        if smallestDivSum <= threshold:
            return num


"""
**************
Optimal Approach
**********************************************
1. The same BS approach will be followed
2. Initially keep the pointer low = 1 and high = maxEle of array
3. Calculate the mid element using (low + high) // 2
4. While loop till low <= high
5. Calculate the sum required for that mid element using a calculateDivSum func, If :
    - It is within the stipulated threshold means we can get a smaller element on left so h = m-1
    - Else l = mid + 1
6. Once done return low ( Do it on a paper you would understand why low will be returned )

TC : O(n * log2(maxEleOfArray))
SC : O(1)
**********************************************
"""

def smallestDiv(nums, threshold):

    maxEle = max(nums)
    low = 1
    high = maxEle

    # Function to calculate calculateDivSum for the middle element.
    def calculateDivSum(nums, mid):

        totalDivSum = 0
        for num in nums:
            totalDivSum += math.ceil(num / mid)

        return totalDivSum

    # Perform BS on the range
    while low <= high:

        mid = (low + high) // 2

        # Calculate totalDivSum for midElement
        totalDivSum = calculateDivSum(nums, mid)

        # If it is within the stipulated threshold, let's check on left if there is any smaller
        # number.
        if totalDivSum <= threshold:
            high = mid - 1

        # Else on right side
        else:
            low = mid + 1

    return low

# Input
nums = [44,22,33,11,1]
threshold = 5
print(smallestDiv(nums, threshold))