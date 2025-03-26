"""
**************
Brute Approach
**********************************************
1. Sort the entire array.

TC : O(n * logN)
SC : O(n)
**********************************************
"""

def sort0s1s2s(nums, n):

    nums.sort()
    return nums


"""
**************
Better Approach
**********************************************
1. Use three variables cnt0, cnt1, cnt2.
2. Iterate through the array and count zero's, one's and two's.
3. Initialize a idx variable initial to zero, now iterate through cnt0 and update idx, same
    for cnt1 and cnt2.
4. Once done, return the array.

TC : O(2n)
SC : O(1)
**********************************************
"""

def sort0s1s2s(nums,n):

    cnt0, cnt1, cnt2 = 0, 0, 0
    # Iterate and get count to zeros, ones and twos.
    for num in nums:
        if num == 0:
            cnt0 += 1
        elif num == 1:
            cnt1 += 1
        else:
            cnt2 += 1

    idx = 0
    # Iterate on cnt0, cnt1 and cnt2. Assign the values first zeros, ones and twos.
    for i in range(cnt0):
        nums[idx] = 0
        idx += 1

    for i in range(cnt1):
        nums[idx] = 1
        idx += 1

    for i in range(cnt2):
        nums[idx] = 2
        idx += 1


"""
**************
Optimal Approach ( Dutch National Flag Algorithm )
**********************************************
                        Algorithm
=====================================================================================
       0  low-1  low  mid-1  mid  high  high+1 n-1 
       |    |     |    |      |    |      |    |
       |    |     |    |      |    |      |    |
       000000     111111      012120      222222
       
The algo states that, the values ranging from

    0 -> low - 1 ======== would be zeros
    low -> mid - 1 ========= would be ones
    mid -> high ========would be the unsorted array
    high + 1 -> n - 1 ============ would be twos
======================================================================================

1. Initialize the variables low and mid to zero and high to length - 1.
2. Traverse through the array till mid crosses high
3. We will be considering mid pointer through out as according to algo mid -> high is unsorted.
4. Case
    * mid equals zero -> swap low and mid and update both pointers
    * mid equals one -> update mid pointer
    * mid equals two -> swap mid and high and decrease high pointer.
5. Loop will break, and the is sorted.

TC : O(n)
SC : O(1)
**********************************************
"""


def sort0s1s2s(arr, n):

    low = 0
    high = n - 1
    mid = 0

    # Perform till mid crosses high
    while mid <= high:
        # If mid is zero, swap low and mid and update both.
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        # If mid is one, update mid pointer
        elif nums[mid] == 1:
            mid += 1

        # If mid is two, then swap mid and high, decrease high
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

# Input
nums = [2,0,2,1,1,0]
n = len(nums)
print(sort0s1s2s(nums,n))