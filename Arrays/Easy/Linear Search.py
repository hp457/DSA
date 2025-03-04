"""
************
Optimal Code
********************************************************************************
1. Iterate through array in a linear fashion and return index or value.
********************************************************************************
"""

def linearSearch(nums):

    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i

    return -1