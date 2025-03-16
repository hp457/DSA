"""
**************
Brute Approach
**********************************************
1. Initialize four variables m -> length of nums1, n -> length of nums2, l = 0, r =0
    and a resultant list res
2. Merge two array into res array using while loop until l exceeds m and r exceeds n
3. Now run another while loop for the remaining elements on the left array
4. Same Step - 3 for right array
5. Now check if (m + n) is odd or even and based on that, return median:
    Odd : Middle Index
    Even : Sum of middle and middle - 1 index

TC : O(m + n)
SC : O(m + n)
**********************************************
"""

def medianOfTwoSortedArray(nums1, nums2):

    m = len(nums1)
    n = len(nums2)
    l = 0
    r = 0
    res = list()

    while l < m and r < n:

        if nums1[l] <= nums2[r]:
            res.append(nums1[l])
            l += 1
        else:
            res.append(nums2[r])
            r += 1

    while l < m:
        res.append(nums1[l])
        l += 1

    while r < n:
        res.append(nums2[r])
        r += 1

    resLen = m + n
    if resLen % 2 == 0:
        return (res[resLen // 2] + res[(resLen // 2) - 1]) / 2
    else:
        return res[resLen // 2]


"""
**************
Better Approach (Reduce Space )
**********************************************
1. Let's say you have an array of even size 4, what would be the median indexes of it. 1 and 2
    And in case of odd size 5, the index would be 3. ( Think it is a single sorted array )
2. We know the indexes now which should be returned. So the approach here we would be following
    is, will keep a counter variable which will hold the indexes.
3. Use the similar approach of merging two sorted arrays.
4. While merging increment the counter every time, so that we would know the indexes.
5. Check if the idx1 and idx2 element is equal to counter, if it then we got the values to
    be returned at the end.
6. If the length is even after merging then return (ele1 + ele2) // 2 else
    return ele2.

TC : O(m+n)
SC : O(1)
**********************************************
"""

def medianOfTwoSortedArray(nums1, nums2):

    m = len(nums1)
    n = len(nums2)
    l = 0
    r = 0
    cnt = 0
    idx1 = (m + n) // 2 - 1
    idx2 = (m + n) // 2
    ele1 = -1
    ele2 = -1

    while l < m and r < n:
        if nums1[l] < nums2[r]:
            if cnt == idx1:
                ele1 = nums1[l]
            if cnt == idx2:
                ele2 = nums1[l]
            l += 1
            cnt += 1

        else:
            if cnt == idx1:
                ele1 = nums2[r]
            if cnt == idx2:
                ele2 = nums2[r]
            r += 1
            cnt += 1

    while l < m:
        if cnt == idx1:
            ele1 = nums1[l]
        if cnt == idx2:
            ele2 = nums1[l]
        l += 1
        cnt += 1

    while r < n:
        if cnt == idx1:
            ele1 = nums2[r]
        if cnt == idx2:
            ele2 = nums2[r]
        r += 1
        cnt += 1

    if (m + n) % 2 == 1:
        return ele2

    return (ele1 + ele2) / 2


# Input
nums1 = [1,2]
nums2 = [3,4]
print(medianOfTwoSortedArray(nums1, nums2))