"""
**************
Brute Approach
**********************************************
1. Initialize four variables m -> length of nums1, n -> length of nums2, l = 0, r =0
    and a resultant list res
2. Merge two array into res array using while loop until l exceeds m and r exceeds n
3. Now run another while loop for the remaining elements on the left array
4. Same Step - 3 for right array
5. Now iterate another loop on the res array and check if index equals k - 1,
    if it is return res[i]

TC : O(m + n)
SC : O(m + n)
**********************************************
"""


def kthElement(nums1, nums2, k):

    m = len(nums1)
    n = len(nums2)
    l, r = 0, 0
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

    resLen = len(res)
    for i in range(resLen):
        if i == k - 1:
            return res[i]


"""
**************
Better Approach (Reduce Space )
**********************************************
1. Initialize a idx to k - 1, the index we are looking for and we need to return.
2. Initialize a counter variable cnt which will hold the indexes.
3. Use the similar approach of merging two sorted array.
4. Within each loop check if cnt equals idx, if it we got the element to be returned, so will
    store that element into a variable kEle.
5. Once the array is merged, return the kEle.

TC : O(m+n)
SC : O(1)
**********************************************
"""


def kthElement(a, b, k):

    m = len(a)
    n = len(b)
    l, r = 0, 0
    idx = k - 1
    cnt = 0
    res = list()
    kEle = -1

    while l < m and r < n:

        if a[l] <= b[r]:
            if cnt == idx:
                kEle = a[l]
            l += 1
            cnt += 1
        else:
            if cnt == idx:
                kEle = b[r]
            r += 1
            cnt += 1

    while l < m:
        if cnt == idx:
            kEle = a[l]
        l += 1
        cnt += 1

    while r < n:
        if cnt == idx:
            kEle = b[r]
        r += 1
        cnt += 1

    return kEle


# Input
nums1 = [2, 3, 6, 7, 9]
nums2 = [1, 4, 8, 10]
k = 5
print(kthElement(nums1, nums2, k))