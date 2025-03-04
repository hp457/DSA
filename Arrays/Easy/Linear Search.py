"""
************
Optimal Code
********************************************************************************
1. Iterate through array in a linear fashion and return index or value.
********************************************************************************
"""

def linearSearch(nums, target):

    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i

    return -1

nums = [1,2,3,4,5]
target = 4
linearSearch(nums,target)
